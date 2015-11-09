#_*_coding:utf-8_*_
__author__ = 'jieli'
import datetime

from django import template
register = template.Library()


@register.filter
def contains(value,arg):

    print '--->str',value,arg
    if arg in value:
        return  True
    else:
        return False