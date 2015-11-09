#_*_coding:utf-8_*_
__author__ = 'Alex Li'

import time
def json_date_handler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.strftime("%Y-%m-%d")