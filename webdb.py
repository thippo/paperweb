# -*- coding:utf-8 -*- 

import pymongo
from pymongo import MongoClient
from bson import ObjectId
from utils import *

client = MongoClient('mongodb://localhost:27017/')

def _get_collection(username):
    db = client[username]
    collection = db['papers']
    return collection

def insert_db(username, content):
    _get_collection(username).insert_one(content)

def get_paper(username, _id):
    a = _get_collection(username).find_one({'_id':ObjectId(_id)})
    return a

def get_tag_papers(username, tag):
    if tag:
        a = list(_get_collection(username).find({'tags':{"$in":[tag]}}))
    else:
        a = list(_get_collection(username).find().limit(5))
    return a

def get_sorted_tags(username):
    a = [y for x in _get_collection(username).find({}, {'tags':1, '_id':0}) for y in x['tags']]
    a = sort_tags(a)
    return a

def remove_paper(username, _id):
    return _get_collection(username).remove({"_id":ObjectId( _id)})

def get_bibtex(username, _id):
    a = _get_collection(username).find_one({'_id':ObjectId(_id)}, {'bibtex':1})
    return a
