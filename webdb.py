import pymongo
from pymongo import MongoClient
from bson import ObjectId
from utils import *

client = MongoClient('mongodb://localhost:27017/')
db = client['thippo']
collection = db['papers']

def insert_db(content):
    collection.insert_one(content)

def get_paper(_id):
    a = collection.find_one({'_id':ObjectId(_id)})
    return str(a)

def get_titles():
    a = list(collection.find({}, {'title':1}).limit(10))
    return a

def get_tag_papers(tag_list):
    a = list(collection.find({'tags':{"$in":tag_list}}, {'title':1}))
    return str(a)

def get_sorted_tags():
    a = [y for x in collection.find({}, {'tags':1, '_id':0}) for y in x['tags']]
    a = sort_tags(a)
    return a

def get_all():
    a = collection.find_one()
    return str(a)
