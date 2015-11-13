#_*_coding:utf-8_*_
__author__ = 'Alex Li'

from plugins import plugin_api
import json


class InfoCollection(object):
    def __init__(self):
        pass


    def get_platform(self):

        platform = 'linux' #needs to be implenmented

        return platform


    def collect(self):
        platform = self.get_platform()

        func = getattr(self,platform)
        info_data = func()
        formatted_data = self.build_report_data(info_data)
        return formatted_data
    def linux(self):
        sys_info = plugin_api.LinuxSysInfo()

        return sys_info
        #for k,v in sys_info.items():
        #    print '%s:\t\t %s'%(k,v)
        #plugin_api.LinuxCpuInfo()

    def build_report_data(self,data):

        #add token info in here before send

        return data
