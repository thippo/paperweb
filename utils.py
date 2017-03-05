# -*- coding:utf-8 -*- 

import collections
from werkzeug.security import generate_password_hash, check_password_hash

def sort_tags(input_list):
    count_dict = collections.Counter(input_list)
    order_dict = collections.OrderedDict(sorted(count_dict.items(), key=lambda t: t[1] ,reverse=True))    
    return order_dict

