#_*_coding:utf-8_*_
__author__ = 'Alex Li'


import models


def get_asset_model(obj):
    asset_tables = ['server','networkdevice','software']
    for asset_type in asset_tables:
        if hasattr(obj,asset_type):
            ass_obj =getattr(obj,asset_type)
            return ass_obj.model
def fetch_asset_list():

    #asset_list = models.Asset.objects.values('id','idc__name','business_unit__name', 'manufactory__manufactory','server__model','asset_type','management_ip','cpu__cpu_model','sn','tags','name','networkdevice','trade_time')
    asset_list = models.Asset.objects.all()
    data_list = []
    for obj in asset_list:
        if obj.asset_type == 'server':
            data = {
                'sn': obj.sn,
                'name': obj.name,
                'id': obj.id,
                'idc': None if not obj.idc else obj.idc.name,
                'business_unit': None if not obj.business_unit else obj.business_unit.name,
                'manufactory': None if not obj.manufactory else obj.manufactory.manufactory,
                'model': get_asset_model(obj),
                'cpu_model' : None if not obj.cpu else obj.cpu.cpu_model,
                'cpu_core_count' : None if not obj.cpu else obj.cpu.cpu_core_count,
                'asset_type': obj.get_asset_type_display(),
                'management_ip': obj.management_ip,
                'ram_size': sum([i.capacity if i.capacity else 0 for i in obj.ram_set.select_related()]),
                'disk_size': sum([i.capacity if i.capacity else 0 for i in obj.disk_set.select_related()]),
                'status': None,
            }
        elif obj.asset_type in ('switch','router','firewall','storage','NLB','wireless'):
            data = {
                'sn': obj.sn,
                'name': obj.name,
                'id': obj.id,
                'idc': None if not obj.idc else obj.idc.name,
                'business_unit': None if not obj.business_unit else obj.business_unit.name,
                'manufactory': None if not obj.manufactory else obj.manufactory.manufactory,
                'model': get_asset_model(obj),
                'cpu_model' : None,
                'cpu_core_count' : None ,
                'asset_type': obj.get_asset_type_display(),
                'management_ip': obj.management_ip,
                'ram_size': None,
                'disk_size': None,
                'status': None,
            }
        print data
        data_list.append(data)
    return  {'data':data_list}


def fetch_asset_event_logs(asset_id):
    log_list = models.EventLog.objects.filter(asset_id= asset_id)
    data_list = []
    for log in log_list:
        data = {
            'id':log.id,
            'event_type':log.get_event_type_display(),
            'name':log.name,
            'component':log.component,
            'detail':log.detail,
            'user':log.user.name,
            'date':log.date,
        }
        data_list.append(data)

    return {"data":data_list}