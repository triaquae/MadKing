#_*_coding:utf-8_*_
__author__ = 'Alex Li'


import hashlib,time



def get_token(username,token_id):
    timestamp = int(time.time())
    md5_format_str = "%s\n%s\n%s" %(username,timestamp,token_id)
    obj = hashlib.md5()
    obj.update(md5_format_str)
    print "token format:[%s]" % md5_format_str
    print "token :[%s]" % obj.hexdigest()
    return obj.hexdigest()[10:17], timestamp


if __name__ =='__main__':
    print get_token('alex','test')