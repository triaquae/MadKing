#_*_coding:utf-8_*_
__author__ = 'Alex Li'

from plugins import plugin_api

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
    def linux(self):
        print plugin_api.LinuxSysInfo()
        #plugin_api.LinuxCpuInfo()

    def build_report_data(self,data):
        pass
