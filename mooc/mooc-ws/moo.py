"""
6, Apr 2013

Example bottle (python) RESTful web service.

This example provides a basic setup of a RESTful service

Notes
1. example should perform better content negotiation. A solution is
   to use minerender (https://github.com/martinblech/mimerender)
"""
// test comment 
import time
import sys
import socket
import json

# bottle framework
from bottle import request, response, route, run, template

# moo
from classroom import Room

# virtual classroom implementation
room = None

def setup(base, conf_fn):
   print '\n**** service initialization ****\n'
   global room 
   room = Room(base, conf_fn)

#
# setup the configuration for our service
@route('/')
def root():
   print "--> root"
   return 'welcome'

#
#
@route('/moo/ping', method='GET')
def ping():
   return 'ping %s - %s' % (socket.gethostname(), time.ctime())

#
# Development only: echo the configuration of the virtual classroom.
#
# Testing using curl:
# curl -i -H "Accept: application/json" http://localhost:8080/moo/conf
#
# WARN: This method should be disabled or password protected - dev only!
#
@route('/moo/conf', method='GET')
def conf():
   fmt = __format(request)
   response.content_type = __response_format(fmt)
   return room.dump_conf(fmt)

#
# example of a RESTful method. This example is very basic, it does not 
# support much in the way of content negotiation.
#
@route('/moo/echo/:msg')
def echo(msg):
   fmt = __format(request)
   response.content_type = __response_format(fmt)
   if fmt == Room.html:
      return '<h1>%s</h1>' % msg
   elif fmt == Room.json:
      rsp = {}
      rsp["msg"] = msg
      return json.dumps(all)
   else:
      return msg


#
# example of a RESTful query
#
#@route('/moo/data/:name', method='GET')
#def find(name):
#   print '---> moo.find:', name
#   return room.find(name)

#
# example adding data using forms
#

@route('/discussion/:id', method='DELETE')
def deleteDiscussion(id):
   print '---> deleteDiscussion.find:'
   return room.deleteDiscussion(id)

@route('/discussion/:id', method='PUT')
def updateDiscussion(id):
   data = json.loads(request.body.getvalue())
   data["_Id"] = id
   return room.updateDiscussion(id, data )
      
@route('/announcement/:id', method='DELETE')
def deleteAnnoucement(id):
   print '---> deleteAnnouncement.find:'
   return room.deleteAnnouncement(id)
      
@route('/course/:id', method='DELETE')
def deleteCourse(id):
   print '---> deleteCourse.find:'
   return room.deleteCourse(id)

@route('/announcement/:id', method='PUT')
def updateAnnoucement(id):
   data = json.loads(request.body.getvalue())
   data["_Id"] = id
   return room.updateAnnoucement(id, data )
      
@route('/course/:id', method='PUT')
def updateCourse(id):
   data = json.loads(request.body.getvalue())
   data["_Id"] = id
   return room.updateCourse(id, data )
      
     
@route('/course/list', method='GET')
def listCourse():
   fmt = __format(request)
   response.content_type = __response_format(fmt)
   print '---> listCourse.find:'
   return room.listCourse()

      
@route('/course/:id', method='GET')
def getCourse(id):
   print '---> moo.getCourse:',id
   return room.getCourse(id)


@route('/moo/data', method='POST')
def add():
   print '---> moo.add'

   # example list form values
   k = request.forms.allitems()
   
   for key, value in k:
      data = json.loads(key)
   return room.add(data['username'], data['password'])

#sign in
@route('/auth', method='POST')
def auth():
  print '---> moo.auth:'
  k = request.forms.allitems()
  for key,value in k:
    data = json.loads(key)
  return room.auth(data['email'],data['pwd'])

#create User
@route('/user', method='POST')
def addUser():
  k = request.forms.allitems()
  for key,value in k:
     data = json.loads(key)
  return room.addUser(data['email'],data['pwd'],data['fname'],data['lname'])

#update User
@route('/user/:email', method='PUT')
def updateUser(email):
    print '---> moo.update user----->>>>'  
    data = json.loads(request.body.getvalue())
    print '---> moo.update user----->>>>'  
    print '---> moo.update user----->>>>' ,data["pwd"]
    return room.updateUser( email, data )

#delete User  
@route('/user/:email', method='DELETE')
def deleteUser(email):
   print '---> moo.find:', email
   return room.deleteUser(email)

@route('/user/:email', method='GET')
def getUser(email):
   print '---> moo.find:', email
   return room.getUser(email)

@route('/course', method='POST')
def addCourse():
   print '---> moo.addCourse'
   k = request.forms.allitems()
   #for key, value in k:
      #data = json.loads(key)
   return room.addCourse(k)

#
#Add category
#
@route('/category', method='POST')
def catadd():
   print '---> sweta : in moo -> category.add'

   # example list form values
   k = request.forms.allitems()
   for key,value in k:
      data = json.loads(key)
   return room.catadd(data['name'],data['description'],data['createDate'],data['status'])


#
# Find category
#
@route('/category/:id', method='GET')
def catfind(id):
   print '---> category.find:',id
   return room.catfind(id)

#
# Find category list
#
@route('/category/list', method='GET')
def catlistfind():
   print '---> categorylist.find:'
   return room.catlistfind()

#
#Add announcement
#
@route('/announcements', method='POST')
def announcementadd():
   print '---> announcement.add'

   # example list form values
   k = request.forms.allitems()
   for key,value in k:
      data = json.loads(key)
   return room.announcementadd(data['courseId'],data['title'],data['description'],data['postDate'],data['status'])



#
# Find announcement
#
@route('/announcement/:id', method='GET')
def announcementfind(id):
   print '---> announcement find:',id
   return room.announcementfind(id)


#
# Find announcement list
#
@route('/announcement/list', method='GET')
def announcementlistfind():
   print '---> announcementlist.find:'
   return room.announcementlistfind()


@route('/moo/data/test', method='POST')
def testForm():
   print '---> moo.testForm'
   k = request.forms.allitems()
   #for key, value in k:
      #data = json.loads(key)
   print k
   payload = {'result':'msg reached'}
   return json.dumps(payload)


#
# Determine the format to return data (does not support images)
#
# TODO method for Accept-Charset, Accept-Language, Accept-Encoding, 
# Accept-Datetime, etc should also exist
#
def __format(request):
   # for key in sorted(request.headers.iterkeys()):
   #   print "%s=%s" % (key, request.headers[key])

   types = request.headers.get("Accept", '')
   subtypes = types.split(",")
   for st in subtypes:
      sst = st.split(';')
      if sst[0] == "text/html":
         return Room.html
      elif sst[0] == "text/plain":
         return Room.text
      elif sst[0] == "application/json":
         return Room.json
      elif sst[0] == "*/*":
         return Room.json

      # TODO
      # xml: application/xhtml+xml, application/xml
      # image types: image/jpeg, etc

   # default
   return Room.html

#
# The content type on the reply
#
def __response_format(reqfmt):
      if reqfmt == Room.html:
         return "text/html"
      elif reqfmt == Room.text:
         return "text/plain"
      elif reqfmt == Room.json:
         return "application/json"
      else:
         return "*/*"
         
      # TODO
      # xml: application/xhtml+xml, application/xml
      # image types: image/jpeg, etc
