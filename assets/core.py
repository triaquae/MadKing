#_*_coding:utf-8_*_
__author__ = 'jieli'

import json
from django.core.exceptions import ObjectDoesNotExist
import models


class Asset(object):
    def __init__(self,request):
        self.request = request
        self.mandatory_fields = ['sn','asset_id','asset_type'] #must contains 'sn' , 'asset_id' and 'asset_type'
        self.field_sets = {
            'asset':['manufactory'],
            'server':['model','cpu_count','cpu_core_count','cpu_model','raid_type','os_type','os_distribution','os_release'],
            'networkdevice':[]
        }
        self.response = {
            'error':[],
            'info':[]
        }

    def response_msg(self,msg_type,key,msg):
        if self.response.has_key(msg_type):
            self.response[msg_type].append({key:msg})
        else:
            raise ValueError
    def mandatory_check(self,data):
        for field in self.mandatory_fields:
            if not data.has_key(field):
                self.response_msg('error','AssetDataInvalid', "The field [%s] is mandatory and not provided in your reporting data" % field)
        try:
            self.asset_obj = models.Asset.objects.get(id=int(data['asset_id']),sn=data['sn'])
        except ObjectDoesNotExist,e:
            self.response_msg('error','AssetDataInvalid', "Cannot find asset object in DB by using asset id [%s] and SN [%s] " % (data['asset_id'],data['sn']))

    def data_is_valid(self):
        data = self.request.POST.get("asset_data")
        if data:
            try:
                data = json.loads(data)
                self.mandatory_check(data)
                self.clean_data = data
                if not self.response['error']:
                    return True
            except ValueError,e:
                self.response_msg('error','AssetDataInvalid', str(e))
        else:
            self.response_msg('error','AssetDataInvalid', "The reported asset data is not valid or provided")

    def __is_new_asset(self):
        if not hasattr(self.asset_obj, self.clean_data['asset_type']):#new asset
            return True
        else:
            return False
    def data_inject(self):
        '''save data into DB,the data_is_valid() must returns True before call this function'''

        self.reformat_components('slot',self.clean_data.get('ram'))
        self.reformat_components('name',self.clean_data.get('nic'))
        if self.__is_new_asset():
            print '\033[32;1m---new asset,going to create----\033[0m'
            self.create_asset()
        else:#asset already already exist , just update it
            print '\033[33;1m---asset already exist ,going to update----\033[0m'

            self.update_asset()
    def reformat_components(self,identify_field,data_set):
        '''This function is used as workround for some components's data structor is big dict ,yet
        the standard structor is list,e.g:
        standard: [{
            "slot": "1I:1:1",
            "capacity": 300,
            "sn": "",
            "model": "",
            "enclosure": "0",
            "iface_type": "SAS"
        },
        {
            "slot": "1I:1:2",
            "capacity": 300,
            "sn": "",
            "model": "",
            "enclosure": "0",
            "iface_type": "SAS"
        }]
        but for some components such as ram:
        {"PROC 2 DIMM 1": {
            "model": "<OUT OF SPEC>",
            "capacity": 0,
            "sn": "Not Specified",
            "manufactory": "UNKNOWN"
        },}

        it uses key as identified field, the key is actually equals slot field in db model field, this unstandard
        data source should be dprecated in the future, now I will just reformat it as workround
        '''
        for k,data in data_set.items():
            data[identify_field] = k
    def __verify_field(self,data_set,field_key,data_type,required=True):
        field_val = data_set.get(field_key)
        if field_val:
            try:
                data_set[field_key] = data_type(field_val)
            except ValueError,e:
                self.response_msg('error','InvalidField', "The field [%s]'s data type is invalid, the correct data type should be [%s] " % (field_key,data_type) )

        elif required == True:
                self.response_msg('error','LackOfField', "The field [%s] has no value provided in your reporting data [%s]" % (field_key,data_set) )



    def create_asset(self):
        func = getattr(self,'_create_%s' % self.clean_data['asset_type'])
        create_obj =func()

    def update_asset(self):
        func = getattr(self,'_update_%s' % self.clean_data['asset_type'])
        create_obj =func()

    def _update_server(self):
        nic = self.__update_asset_component(data_source=self.clean_data['nic'],
                                            fk='nic_set',
                                            update_fields = ['name','sn','model','macaddress','ipaddress','netmask','bonding'],
                                            identify_field = 'macaddress'
                                            )
        disk = self.__update_asset_component(data_source=self.clean_data['physical_disk_driver'],
                                             fk='disk_set',
                                            update_fields = ['slot','sn','model','manufactory','capacity','iface_type'],
                                            identify_field = 'slot'
                                            )
        ram = self.__update_asset_component(data_source=self.clean_data['ram'],
                                             fk='ram_set',
                                            update_fields = ['slot','sn','model','capacity'],
                                            identify_field = 'slot'
                                            )
        cpu = self.__update_cpu_component()
        manufactory = self.__update_manufactory_component()

        server = self.__update_server_component()
    def _create_server(self):
        self.__create_server_info()
        self.__create_or_update_manufactory()

        cpu_obj = self.__create_cpu_component()
        self.__create_disk_component()
        self.__create_nic_component()
        self.__create_ram_component()


    def __create_server_info(self,ignore_errs=False):
        try:
            self.__verify_field(self.clean_data,'model',str)
            if not len(self.response['error']) or ignore_errs == True: #no processing when there's no error happend
                data_set = {
                    'asset_id' : self.asset_obj.id,
                    'raid_type': self.clean_data.get('raid_type'),
                    'model':self.clean_data.get('model'),
                    'os_type':self.clean_data.get('os_type'),
                    'os_distribution':self.clean_data.get('os_distribution'),
                    'os_release':self.clean_data.get('os_release'),
                }

                obj = models.Server(**data_set)
                obj.save()
                return obj
        except Exception,e:
            self.response_msg('error','ObjectCreationException','Object [server] %s' % str(e) )
    def __create_or_update_manufactory(self,ignore_errs=False):
        try:
            self.__verify_field(self.clean_data,'manufactory',str)
            manufactory = self.clean_data.get('manufactory')
            if not len(self.response['error']) or ignore_errs == True: #no processing when there's no error happend
                obj_exist = models.Manufactory.objects.filter(manufactory=manufactory)
                if obj_exist:
                    obj = obj_exist[0]
                else:#create a new one
                    obj = models.Manufactory(manufactory=manufactory)
                    obj.save()
                self.asset_obj.manufactory = obj
                self.asset_obj.save()
        except Exception,e:
            self.response_msg('error','ObjectCreationException','Object [manufactory] %s' % str(e) )
    def __create_cpu_component(self,ignore_errs=False):
        try:
            self.__verify_field(self.clean_data,'model',str)
            self.__verify_field(self.clean_data,'cpu_count',int)
            self.__verify_field(self.clean_data,'cpu_core_count',int)
            if not len(self.response['error']) or ignore_errs == True: #no processing when there's no error happend
                data_set = {
                    'asset_id' : self.asset_obj.id,
                    'cpu_model': self.clean_data.get('cpu_model'),
                    'cpu_count':self.clean_data.get('cpu_count'),
                    'cpu_core_count':self.clean_data.get('cpu_core_count'),
                }

                obj = models.CPU(**data_set)
                obj.save()
                return obj
        except Exception,e:
            self.response_msg('error','ObjectCreationException','Object [cpu] %s' % str(e) )
    def __create_disk_component(self):
        disk_info = self.clean_data.get('physical_disk_driver')
        if disk_info:
            for disk_item in disk_info:
                try:
                    self.__verify_field(disk_item,'slot',str)
                    self.__verify_field(disk_item,'capacity',float)
                    self.__verify_field(disk_item,'iface_type',str)
                    self.__verify_field(disk_item,'model',str)
                    if not len(self.response['error']): #no processing when there's no error happend
                        data_set = {
                            'asset_id' : self.asset_obj.id,
                            'sn': disk_item.get('sn'),
                            'slot':disk_item.get('slot'),
                            'capacity':disk_item.get('capacity'),
                            'model':disk_item.get('model'),
                            'iface_type':disk_item.get('iface_type'),
                            'manufactory':disk_item.get('manufactory'),
                        }

                        obj = models.Disk(**data_set)
                        obj.save()

                except Exception,e:
                    self.response_msg('error','ObjectCreationException','Object [disk] %s' % str(e) )
        else:
                self.response_msg('error','LackOfData','Disk info is not provied in your reporting data' )
    def __create_nic_component(self):
        nic_info = self.clean_data.get('nic')
        if nic_info:
            for nic_name,nic_item in nic_info.items():
                try:
                    self.__verify_field(nic_item,'macaddress',str)
                    if not len(self.response['error']): #no processing when there's no error happend
                        data_set = {
                            'asset_id' : self.asset_obj.id,
                            'name': nic_name,
                            'sn': nic_item.get('sn'),
                            'macaddress':nic_item.get('macaddress'),
                            'ipaddress':nic_item.get('ipaddress'),
                            'bonding':nic_item.get('bonding'),
                            'model':nic_item.get('model'),
                            'netmask':nic_item.get('netmask'),
                        }

                        obj = models.NIC(**data_set)
                        obj.save()

                except Exception,e:
                    self.response_msg('error','ObjectCreationException','Object [nic] %s' % str(e) )
        else:
                self.response_msg('error','LackOfData','NIC info is not provied in your reporting data' )
    def __create_ram_component(self):
        ram_info = self.clean_data.get('ram')
        if ram_info:
            for ram_name,ram_item in ram_info.items():
                try:
                    self.__verify_field(ram_item,'capacity',int)
                    if not len(self.response['error']): #no processing when there's no error happend
                        data_set = {
                            'asset_id' : self.asset_obj.id,
                            'slot': ram_name,
                            'sn': ram_item.get('sn'),
                            'capacity':ram_item.get('capacity'),
                            'model':ram_item.get('model'),
                        }

                        obj = models.RAM(**data_set)
                        obj.save()

                except Exception,e:
                    self.response_msg('error','ObjectCreationException','Object [ram] %s' % str(e) )
        else:
                self.response_msg('error','LackOfData','RAM info is not provied in your reporting data' )

    def __update_server_component(self):
        update_fields = ['model','raid_type','os_type','os_distribution','os_release']
        if self.asset_obj.server:
            self.__compare_componet(model_obj=self.asset_obj.server,
                                    fields_from_db=update_fields ,
                                    data_source=self.clean_data)
        else:
            self.__create_server_info(ignore_errs=True)

    def __update_manufactory_component(self):
        self.__create_or_update_manufactory(ignore_errs=True)

    def __update_cpu_component(self):
        update_fields = ['cpu_model','cpu_count','cpu_core_count']
        if self.asset_obj.cpu:
            self.__compare_componet(model_obj=self.asset_obj.cpu,
                                    fields_from_db=update_fields,
                                    data_source=self.clean_data)
        else:
            self.__create_cpu_component(ignore_errs=True)
    def __update_asset_component(self,data_source,fk,update_fields,identify_field=None):
        '''
        data_source: the data source of this component from reporting data
        fk: which key to use to find the connection between main Asset obj and each asset component
        update_fields: what fields in DB will be compared and updated
        identify_field: use this field to identify each component of an Asset , if set to None,means only use asset id to identify
         '''
        print data_source,update_fields,identify_field
        try:
            component_obj = getattr(self.asset_obj,fk)
            if hasattr(component_obj,'select_related'): # this component is reverse m2m relation with Asset model
                objects_from_db = component_obj.select_related()
                for obj in objects_from_db:
                    key_field_data= getattr(obj,identify_field)
                    #use this key_field_data to find the relative data source from reporting data
                    if type(data_source) is list:
                        for source_data_item  in data_source:
                            key_field_data_from_source_data = source_data_item.get(identify_field)
                            if key_field_data_from_source_data:
                                if key_field_data == key_field_data_from_source_data: #find the matched source data for this component,then should compare each field in this component to see if there's any changes since last update
                                   self.__compare_componet(model_obj=obj,fields_from_db=update_fields,data_source=source_data_item)
                                   break #must break ast last ,then if the loop is finished , logic will goes for ..else part,then you will know that no source data is matched for by using this key_field_data, that means , this item is lacked from source data, it makes sense when the hardware info got changed. e.g: one of the RAM is broken, sb takes it away,then this data will not be reported in reporting data
                            else: #key field data from source data cannot be none
                                self.response_msg('error','AssetUpdateWarning',"Asset component [%s]'s key field [%s] is not provided in reporting data " % (fk,identify_field) )

                        else:#couldn't find any matches, the asset component must be broken or changed manually
                            print '\033[33;1mWarning:cannot find any matches in source data by using key field val [%s],component data is missing in reporting data!\033[0m' %(key_field_data)
                    elif type(data_source) is dict :
                        for key,source_data_item  in data_source.items():
                            key_field_data_from_source_data = source_data_item.get(identify_field)
                            if key_field_data_from_source_data:
                                if key_field_data == key_field_data_from_source_data: #find the matched source data for this component,then should compare each field in this component to see if there's any changes since last update
                                   self.__compare_componet(model_obj=obj,fields_from_db=update_fields,data_source=source_data_item)
                                   break #must break ast last ,then if the loop is finished , logic will goes for ..else part,then you will know that no source data is matched for by using this key_field_data, that means , this item is lacked from source data, it makes sense when the hardware info got changed. e.g: one of the RAM is broken, sb takes it away,then this data will not be reported in reporting data
                            else: #key field data from source data cannot be none
                                self.response_msg('error','AssetUpdateWarning',"Asset component [%s]'s key field [%s] is not provided in reporting data " % (fk,identify_field) )

                        else:#couldn't find any matches, the asset component must be broken or changed manually
                            print '\033[33;1mWarning:cannot find any matches in source data by using key field val [%s],component data is missing in reporting data!\033[0m' %(key_field_data)
                    else:
                        print '\033[31;1mMust be sth wrong,logic should goes to here at all.\033[0m'
                #compare all the components from DB with the data source from reporting data
                self.__filter_add_or_deleted_components(model_obj_name=component_obj.model._meta.object_name, data_from_db=objects_from_db,data_source=data_source,identify_field=identify_field)

            else:#    this component is reverse fk relation with Asset model
                pass
        except ValueError,e:
            print '\033[41;1m%s\033[0m' % str(e)

    def __filter_add_or_deleted_components(self,model_obj_name,data_from_db,data_source,identify_field):
        '''This function is filter out all  component data in db but missing in reporting data, and all the data in reporting data but not in DB'''
        print data_from_db,data_source,identify_field
        data_source_key_list = []
        if type(data_source) is list:
            for data in data_source:
                data_source_key_list.append(data.get(identify_field))
        elif type(data_source) is dict:
            for key,data in data_source.items():
                if data.get(identify_field):
                    data_source_key_list.append(data.get(identify_field))
                else:#workround for some component uses key as identified field e.g: ram
                    data_source_key_list.append(key)
        print '-->identify field [%s] from db  :',data_source_key_list
        print '-->identify[%s] from data source:',[getattr(obj,identify_field) for obj in data_from_db]

        data_source_key_list = set(data_source_key_list)
        data_identify_val_from_db = set([getattr(obj,identify_field) for obj in data_from_db])
        data_only_in_db= data_identify_val_from_db - data_source_key_list #delete all this from db
        data_only_in_data_source=  data_source_key_list - data_identify_val_from_db #add into db
        print '\033[31;1mdata_only_in_db:\033[0m' ,data_only_in_db
        print '\033[31;1mdata_only_in_data source:\033[0m' ,data_only_in_data_source
        self.__delete_components(all_components=data_from_db, delete_list = data_only_in_db, identify_field=identify_field )
        if data_only_in_data_source:
            self.__add_components(model_obj_name=model_obj_name,all_components=data_source, add_list = data_only_in_data_source, identify_field=identify_field )

    def __add_components(self,model_obj_name,all_components,add_list,identify_field ):
        model_class = getattr(models,model_obj_name)
        will_be_creating_list = []
        print '--add component list:',add_list
        if type(all_components) is list:
            for data in all_components:
                if data[identify_field] in add_list:
                    #print data
                    will_be_creating_list.append(data)
        elif type(all_components) is dict:
            for k,data in all_components.items():
                #workround for some components uses key as identified field ,e.g ram
                if data.get(identify_field):
                    if data[identify_field]  in add_list:
                        #print k,data
                        will_be_creating_list.append(data)
                else: #if the identified field cannot be found from data set,then try to compare the dict key
                    if k in add_list:
                        data[identify_field] = k #add this key into dict , because this dict will be used to create new component item in DB
                        will_be_creating_list.append(data)

        #creating components
        try:
            for component in will_be_creating_list:
                data_set = {}
                for field in model_class.auto_create_fields:
                    data_set[field] = component.get(field)
                data_set['asset_id'] = self.asset_obj.id
                obj= model_class(**data_set)
                obj.save()
                print '\033[32;1mCreated component with data:\033[0m', data_set
                self.response_msg('info','NewComponentAdded',"Asset[%s] --> component[%s] has justed added a new item [%s]" %(self.asset_obj,model_obj_name,data_set))

        except Exception,e:
            print "\033[31;1m %s \033[0m"  % e
    def __delete_components(self,all_components, delete_list , identify_field ):
        '''All the objects in delete list will be deleted from DB'''
        deleting_obj_list = []
        print '--deleting components',delete_list,identify_field
        for obj in all_components:
            val  = getattr(obj,identify_field)
            if val in delete_list:
                deleting_obj_list.append(obj)

        for i in deleting_obj_list:
            i.delete()
            self.response_msg('info','HardwareChanges',"Asset[%s] --> component[%s] --> is lacking from reporting source data, assume it has been removed\replaced,will also delete it from DB has changed from" %(self.asset_obj,i))


    def __compare_componet(self,model_obj,fields_from_db,data_source):
        #print '---going to compare:[%s]' % model_obj,fields_from_db
        #print '---source data:', data_source
        for field in fields_from_db:
            val_from_db = getattr(model_obj,field)
            val_from_data_source = data_source.get(field)
            if val_from_data_source:
                if type(val_from_db) is unicode:val_from_data_source = unicode(val_from_data_source)
                elif type(val_from_db) is int:val_from_data_source = int(val_from_data_source)
                elif type(val_from_db) is float:val_from_data_source = float(val_from_data_source)
                if val_from_db == val_from_data_source:# this field haven't changed since last update
                    pass
                    #print '\033[32;1m val_from_db[%s]  == val_from_data_source[%s]\033[0m' %(val_from_db,val_from_data_source)
                else:
                    print '\033[34;1m val_from_db[%s]  != val_from_data_source[%s]\033[0m' %(val_from_db,val_from_data_source)
                    db_field = model_obj._meta.get_field(field)
                    db_field.save_form_data(model_obj, val_from_data_source)
                    self.response_msg('info','FieldChanged',"Asset[%s] --> component[%s] --> field[%s] has changed from [%s] to [%s]" %(self.asset_obj,model_obj,field,val_from_db,val_from_data_source))
            else:
                self.response_msg('error','AssetUpdateWarning',"Asset component [%s]'s field [%s] is not provided in reporting data " % (model_obj,field) )

        model_obj.save()



class CPUUpdateMgr(object):
    model = models.CPU
    update_fields = ['model','cpu_count','cpu_core_count']
    #exclue_fields = []

class NICUpdateMgr(object):
    model = models.NIC
    identify_fields = ['macaddress']
    update_fields = []
    #exclue_fields = []

