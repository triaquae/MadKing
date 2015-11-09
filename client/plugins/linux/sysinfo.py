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

    data = {}
    data['manufactory'] = raw_data['Manufacturer']
    data['sn'] = raw_data['Serial Number']
    data['model'] = raw_data['Product Name']
    data['uuid'] = raw_data['UUID']
    data['wake_up_type'] = raw_data['Wake-up Type']

    data.update(cpuinfo())

    return data





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

