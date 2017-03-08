# -*- coding:utf-8 -*- 

import collections
import os
import hashlib
from werkzeug.security import generate_password_hash, check_password_hash

def sort_tags(input_list):
    count_dict = collections.Counter(input_list)
    order_dict = collections.OrderedDict(sorted(count_dict.items(), key=lambda t: t[1] ,reverse=True))    
    return order_dict

def save_pdf_file(pdffile):
    filemd5 = hashlib.md5()
    filemd5.update(pdffile.read())
    filemd5name = filemd5.hexdigest()
    if not os.path.exists('static/papers/'+filemd5name+'.pdf'):
        pdffile.seek(0)
        pdffile.save('static/papers/'+filemd5name+'.pdf')
    return filemd5name 
