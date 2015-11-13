#_*_coding:utf-8_*_
__author__ = 'Alex Li'

from linux import sysinfo




def LinuxSysInfo():
    #print __file__
    return  sysinfo.collect()


def WindowsSysInfo():
    from windows import sysinfo as win_sysinfo
    return win_sysinfo.collect()
