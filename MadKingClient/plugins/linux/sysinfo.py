#_*_coding:utf-8_*_
__author__ = 'Alex Li'


import os,sys,subprocess

def collect():
    filter_keys = ['Manufacturer','Serial Number','Product Name','UUID','Wake-up Type']
    raw_data = {}

    for key in filter_keys:
        try:
            cmd_res = subprocess.check_output("sudo dmidecode -t system|grep '%s'" %key,shell=True)
            cmd_res = cmd_res.strip()

            res_to_list = cmd_res.split(':')
            if len(res_to_list)> 1:#the second one is wanted string
                raw_data[key] = res_to_list[1].strip()
            else:

                raw_data[key] = -1
        except Exception,e:
            print e
            raw_data[key] = -2 #means cmd went wrong

    data = {"asset_type":'server'}
    data['manufactory'] = raw_data['Manufacturer']
    data['sn'] = raw_data['Serial Number']
    data['model'] = raw_data['Product Name']
    data['uuid'] = raw_data['UUID']
    data['wake_up_type'] = raw_data['Wake-up Type']

    data.update(cpuinfo())
    data.update(osinfo())
    data.update(raminfo())
    data.update(nicinfo())
    data.update(diskinfo())
    return data


def diskinfo():

    return {'physical_disk_driver':[]}
def nicinfo():
    #tmp_f = file('/tmp/bonding_nic').read()
    raw_data= subprocess.check_output("ifconfig -a",shell=True)
    #raw_data= tmp_f.split("\n")

    nic_dic = {}
    next_ip_line = False
    last_mac_addr = None
    for line in raw_data:
        if next_ip_line:
            #print last_mac_addr
            #print line #, last_mac_addr.strip()
            next_ip_line = False
            nic_name = last_mac_addr.split()[0]
            mac_addr = last_mac_addr.split("HWaddr")[1].strip()
            raw_ip_addr = line.split("inet addr:")
            raw_bcast = line.split("Bcast:")
            raw_netmask = line.split("Mask:")
            if len(raw_ip_addr) > 1: #has addr
                ip_addr = raw_ip_addr[1].split()[0]
                network = raw_bcast[1].split()[0]
                netmask =raw_netmask[1].split()[0]
                #print(ip_addr,network,netmask)
            else:
                ip_addr = None
                network = None
                netmask = None
            if mac_addr not in nic_dic:
                nic_dic[mac_addr] = {'name': nic_name,
                                     'macaddress': mac_addr,
                                     'netmask': netmask,
                                     'network': network,
                                     'bonding': 0,
                                     'model': 'unknown',
                                     'ipaddress': ip_addr,
                                     }
            else: #mac already exist , must be boding address
                if '%s_bonding_addr' %(mac_addr) not in nic_dic:
                    random_mac_addr = '%s_bonding_addr' %(mac_addr)
                else:
                    random_mac_addr = '%s_bonding_addr2' %(mac_addr)

                nic_dic[random_mac_addr] = {'name': nic_name,
                                     'macaddress':random_mac_addr,
                                     'netmask': netmask,
                                     'network': network,
                                     'bonding': 1,
                                     'model': 'unknown',
                                     'ipaddress': ip_addr,
                                     }

        if "HWaddr" in line:
            #print line
            next_ip_line = True
            last_mac_addr = line


    nic_list= []
    for k,v in nic_dic.items():
        nic_list.append(v)

    return {'nic':nic_list}
def raminfo():
    raw_data = subprocess.check_output(["sudo", "dmidecode" ,"-t", "17"])
    raw_list = raw_data.split("\n")
    raw_ram_list = []
    item_list = []
    for line in raw_list:

        if line.startswith("Memory Device"):
            raw_ram_list.append(item_list)
            item_list =[]
        else:
            item_list.append(line.strip())

    ram_list = []
    for item in raw_ram_list:
        item_ram_size = 0
        ram_item_to_dic = {}
        for i in item:
            #print i
            data = i.split(":")
            if len(data) ==2:
                key,v = data

                if key == 'Size':
                    #print key ,v
                    if  v.strip() != "No Module Installed":
                        ram_item_to_dic['capacity'] =  v.split()[0].strip() #e.g split "1024 MB"
                        item_ram_size = int(v.split()[0])
                        #print item_ram_size
                    else:
                        ram_item_to_dic['capacity'] =  0

                if key == 'Type':
                    ram_item_to_dic['model'] =  v.strip()
                if key == 'Manufacturer':
                    ram_item_to_dic['manufactory'] =  v.strip()
                if key == 'Serial Number':
                    ram_item_to_dic['sn'] =  v.strip()
                if key == 'Asset Tag':
                    ram_item_to_dic['asset_tag'] =  v.strip()
                if key == 'Locator':
                    ram_item_to_dic['slot'] =  v.strip()

                #if i.startswith("")
        if item_ram_size == 0:  # empty slot , need to report this
            pass
        else:
            ram_list.append(ram_item_to_dic)

    #get total size(mb) of ram as well
    raw_total_size = subprocess.check_output(" cat /proc/meminfo|grep MemTotal ",shell=True).split(":")
    ram_data = {'ram':ram_list}
    if len(raw_total_size) == 2:#correct

        total_mb_size = int(raw_total_size[1].split()[0]) / 1024
        ram_data['ram_size'] =  total_mb_size
        #print(ram_data)

    return ram_data
def osinfo():
    distributor = subprocess.check_output(" lsb_release -a|grep 'Distributor ID'",shell=True).split(":")
    release  = subprocess.check_output(" lsb_release -a|grep Description",shell=True).split(":")
    data_dic ={
        "os_distribution": distributor[1].strip() if len(distributor)>1 else None,
        "os_release":release[1].strip() if len(release)>1 else None,
        "os_type": "linux",
    }
    #print(data_dic)
    return data_dic
def cpuinfo():
    base_cmd = 'cat /proc/cpuinfo'

    raw_data = {
        'cpu_model' : "%s |grep 'model name' |head -1 " % base_cmd,
        'cpu_count' :  "%s |grep  'processor'|wc -l " % base_cmd,
        'cpu_core_count' : "%s |grep 'cpu cores' |awk -F: '{SUM +=$2} END {print SUM}'" % base_cmd,
    }

    for k,cmd in raw_data.items():
        try:
            cmd_res = subprocess.check_output(cmd,shell=True)
            raw_data[k] = cmd_res.strip()

        #except Exception,e:
        except ValueError,e:
            print e

    data = {
        "cpu_count" : raw_data["cpu_count"],
        "cpu_core_count": raw_data["cpu_core_count"]
        }
    cpu_model = raw_data["cpu_model"].split(":")
    if len(cpu_model) >1:
        data["cpu_model"] = cpu_model[1].strip()
    else:
        data["cpu_model"] = -1



    return data


if __name__=="__main__":
    nicinfo()