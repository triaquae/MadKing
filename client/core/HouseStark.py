#_*_coding:utf-8_*_
__author__ = 'Alex Li'

import info_collection
class ArgvHandler(object):
    def __init__(self,argv_list):
        self.argvs = argv_list
        self.parse_argv()


    def parse_argv(self):
        if len(self.argvs) >1:
            if hasattr(self,self.argvs[1]):
                func = getattr(self,self.argvs[1])
                func()
            else:
                self.help_msg()
        else:
            self.help_msg()
    def help_msg(self):
        msg = '''
        collect_data
        run_forever
        '''
        print msg

    def collect_data(self):
        obj = info_collection.InfoCollection()
        obj.collect()

    def run_forever(self):
        pass