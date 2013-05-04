"""
Storage interface
"""
#! /usr/bin/python
import time
from pymongo import Connection
from bson import json_util
import json


class Storage(object):
    def __init__(self):
        # initialize our storage, data is a placeholder
        self.data = {}
        # for demo
        self.data['created'] = time.ctime()

    def insert(self, name, value):
        connection = Connection()
        db = connection['cmpe275-project2']
        try:
            user = {"username": name, "password": value}
            users = db['users']
            users.insert(user)
            return "added"
        except:
            return "error: data not added"

    def remove(self, name):
        print "---> remove:", name

    def names(self):
        print "---> names:"
        for k in self.data.iterkeys():
            print 'key:', k

    def find(self, name):
        print "---> storage.find:", name
        connection = Connection()
        db = connection['cmpe275-project2']
        c = db.users.find({"username": 'john'}).count()
        print "Count-->", c
        st = {"username": name}
        print "String-->", st
        name1 = db.users.find(st)
        print name1.count()
        for record in name1:
            print "--> Inside Cursor"
            del record["_id"]
            json.dumps(record)
            print "Record:", record
        if name > 0:
            return record
        else:
            return None
