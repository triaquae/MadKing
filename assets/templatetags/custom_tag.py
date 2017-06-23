#_*_coding:utf-8_*_
__author__ = 'jieli'
import datetime
from  django.core.urlresolvers import reverse as url_reverse

from django import template
from django.utils.safestring import mark_safe
import re

register = template.Library()


@register.filter
def contains(value,arg):

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


@register.simple_tag
def get_table_column(column, table_obj):
    print(table_obj.model_class)
    try:
        column_name = table_obj.model_class._meta.get_field(column).verbose_name
    except Exception as e:
        print("ee",e)
        column_name = getattr(table_obj.model_class,column)
    return  column_name


@register.simple_tag
def get_fk_table_column(column, table_obj):
    print(table_obj.model_class)
    dy_fk = getattr(table_obj,table_obj.model_class.dynamic_fk)
    dy_fk_class = getattr(table_obj.model_class,dy_fk)
    # column_name = dy
    # return  table_obj.model_class._meta.get_field(column).verbose_name
    #

@register.simple_tag
def build_table_row(row_obj,table_obj,onclick_column=None,target_link=None):
    print('--->onclick', onclick_column,)
    row_ele = "<tr>"
    for index,column_name in enumerate(table_obj.list_display):
        try:
            column_data = row_obj._meta.get_field(column_name)._get_val_from_obj(row_obj)
        except Exception as e:
            if hasattr(row_obj,column_name):
                column_data = getattr(row_obj,column_name)()
            else:
                raise  ValueError

        if column_name in table_obj.choice_fields:
            column_data = getattr(row_obj,'get_%s_display'%column_name)()
        if column_name in table_obj.fk_fields:
            column_data = getattr(row_obj,column_name).__str__()
        if onclick_column == column_name:
            column = ''' <td><a href=%s>%s</a></td> '''% (url_reverse(target_link,args=(column_data, )),column_data)
        else:
            column = "<td>%s</td>" % column_data
        row_ele +=column

    #for dynamic display
    if table_obj.dynamic_fk :
        if hasattr(row_obj,table_obj.dynamic_fk ):
            #print("----dynamic:",getattr(row_obj,table_obj.dynamic_fk), row_obj)
            #print(row_obj.networkdevice)
            dy_fk = getattr(row_obj,table_obj.dynamic_fk) #拿到的是asset_type的值
            if hasattr(row_obj,dy_fk):
                dy_fk_obj = getattr(row_obj,dy_fk)
                print("-->type",type(dy_fk_obj), dy_fk_obj )
                for index,column_name in enumerate(table_obj.dynamic_list_display):
                    if hasattr(dy_fk_obj,column_name):
                        if column_name in table_obj.dynamic_choice_fields:
                            column_data = getattr(dy_fk_obj, 'get_%s_display' % column_name)()
                        else:
                            column_data = dy_fk_obj._meta.get_field(column_name)._get_val_from_obj(dy_fk_obj)
                        print("dynamic column data", column_data)

                        column = "<td>%s</td>" % column_data
                    else:
                        column = "<td>n/a</td>"
                    row_ele += column
            else:
                #这个关联的表还没创建呢， 但也要创建空的html td占位符
                for index, column_name in enumerate(table_obj.dynamic_list_display):
                    row_ele +="<td></td>"

    for field in table_obj.m2m_fields:
        m2m_obj = getattr(row_obj,field)
        column = "<td> "
        for obj in m2m_obj.select_related():
            column += "<span style='display:inline-block' class='label label-mint label-info'>%s</span>" % obj.__str__()
        column += "</td>"
        row_ele += column
    row_ele += "</tr>"
    return mark_safe(row_ele)

@register.simple_tag
def render_page_num(request,paginator_obj,loop_counter):
    abs_full_url = request.get_full_path()

    if "?page=" in abs_full_url:
        url = re.sub("page=\d+", "page=%s" % loop_counter, request.get_full_path())
    elif "?" in abs_full_url:
        url = "%s&page=%s" % (request.get_full_path(), loop_counter)
    else:
        url = "%s?page=%s" % (request.get_full_path(), loop_counter)


    if loop_counter == paginator_obj.number: #current page
        return mark_safe('''<li class='active'><a href="{abs_url}">{page_num}</a></li>'''\
            .format(abs_url=url,page_num=loop_counter))


    if abs(loop_counter - paginator_obj.number) <2 or \
        loop_counter == 1 or loop_counter == paginator_obj.paginator.num_pages: #the first page or last

        return mark_safe('''<li><a href="{abs_url}">{page_num}</a></li>'''\
            .format(abs_url= url,page_num=loop_counter))
    elif abs(loop_counter - paginator_obj.number) <3:
        return mark_safe('''<li><a href="{abs_url}">...</a></li>'''\
            .format(abs_url=url ,page_num=loop_counter))
    else:
        return ''


@register.simple_tag
def display_orderby_arrow(table_obj,loop_counter):
    if table_obj.orderby_col_index == loop_counter:
        if table_obj.orderby_field.startswith('-'):#降序
            orderby_icon = '''<i class="fa fa-caret-up" aria-hidden="true"></i>'''
        else:
            orderby_icon = '''<i class="fa fa-caret-down" aria-hidden="true"></i>'''
        return mark_safe(orderby_icon)
    return ''

@register.filter
def to_string(value):
    return '%s' %value
