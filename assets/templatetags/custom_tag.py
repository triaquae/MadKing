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


@register.filter
def sum_size(data_set):
    total_val = sum([i.capacity if i.capacity else 0 for i in data_set])

    return total_val


@register.filter
def list_count(data_set):
    data_count = len([i.capacity if i.capacity else 0 for i in data_set])

    return data_count