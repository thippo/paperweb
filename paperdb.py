# -*- coding:utf-8 -*- 

from mongodbclient import client
from bson import ObjectId
from utils import *

def _get_collection(username):
    db = client[username]
    collection = db['papers']
    return collection

def insert_db(username, content):
    _get_collection(username).insert_one(content)

def get_paper(username, _id):
    a = _get_collection(username).find_one({'_id':ObjectId(_id)})
    return a

def get_tag_papers_count(username, tag):
    if tag:
        a = _get_collection(username).find({'tags':{"$in":[tag]}}).sort([('date',-1)]).count()
    else:
        a = _get_collection(username).find().sort([('date',-1)]).count()
    return a

def get_tag_pagination_papers(username, tag, page):
    if tag:
        a = list(_get_collection(username).find({'tags':{"$in":[tag]}}).sort([('date',-1)]).skip((int(page)-1)*5).limit(5))
    else:
        a = list(_get_collection(username).find().sort([('date',-1)]).skip((int(page)-1)*5).limit(5))
    return a

def get_sorted_tags(username):
    a = [y for x in _get_collection(username).find({}, {'tags':1, '_id':0}) for y in x['tags']]
    a = sort_tags(a)
    return a

def update_paper(username, _id, description, tags, pdfweb, secret):
    return  _get_collection(username).update({'_id':ObjectId(_id)}, {'$set':{'description':description, 'tags':tags, 'pdfweb':pdfweb, 'secret':secret}})

def remove_paper(username, _id):
    return _get_collection(username).remove({"_id":ObjectId( _id)})

def get_bibtex(username, _id):
    a = _get_collection(username).find_one({'_id':ObjectId(_id)}, {'bibtex':1})
    return a

def get_secret(username, _id):
    try:
        a = _get_collection(username).find_one({'_id':ObjectId(_id)}, {'secret':1})
        if a:
            return a['secret']
        else:
            return True
    except:
        return True

def update_secret(username, _id, secret):
    try:
        _get_collection(username).update({'_id':ObjectId(_id)}, {'$set':{'secret':secret}})
        return True
    except:
        return False
