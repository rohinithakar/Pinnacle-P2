"""
6, Apr 2013

Example domain logic for the RESTful web service example.

This class provides basic configuration, storage, and logging.
"""

import sys
import os
import socket
import StringIO
import json
import traceback

# moo 
from data.storage import Storage

#
# Room (virtual classroom -> Domain) functionality - note this is separated 
# from the RESTful implementation (bottle)
#
# TODO: only return objects/data and let moo.py handle formatting through 
# templates
#
class Room(object):
   # very limited content negotiation support - our format choices 
   # for output. This also shows _a way_ of representing enums in python
   json, xml, html, text = range(1, 5)
   
   #
   # setup the configuration for our service
   #
   def __init__(self, base, conf_fn):
      self.host = socket.gethostname()
      self.base = base
      self.conf = {}
      
      # should emit a failure (file not found) message
      if os.path.exists(conf_fn):
         with open(conf_fn) as cf:
            for line in cf:
               name, var = line.partition("=")[::2]
               self.conf[name.strip()] = var.strip()
      else:
         raise Exception("configuration file not found.")

      # create storage
      self.__store = Storage()
   
   
   #
   # example: get course
   #
   def getCourse(self, id):
      print '---> classroom.getCourse:',id
      return self.__store.getCourse(id)
  
  
   #
   # example: add data
   #
   def add(self,name,value):
      try:
         self.__store.insert(name,value)
         self.__store.names();
         return 'success'
      except:
         e = sys.exc_info()[0]
         traceback.print_exc(file=sys.stdout)
         return "Error: %s" % e

      # TODO success|failure
      
             # update Annoucement

   def updateDiscussion(self, id, body):
       self.__store.updateDiscussion(id, body)
      
          # update Annoucement

   def updateAnnoucement(self, id, body):
       self.__store.updateAnnoucement(id, body)
       
            #
    # Discussion list delete
   #
   def deleteDiscussion(self, id):
          print '---> classroom discussion delete.find:'
          try:
              return self.__store.deleteDiscussion(id)
          except:
              e = sys.exc_info()[0]
              traceback.print_exc(file=sys.stdout)
              return "Error: %s" % e
       
       #
    # Announcement list delete
   #
   def deleteAnnouncement(self, id):
          print '---> classroom announcement delete.find:'
          try:                
                return self.__store.deleteAnnouncement(id)
          except:
              e = sys.exc_info()[0]
              traceback.print_exc(file=sys.stdout)
              return "Error: %s" % e
      
      # update course

   def updateCourse(self, id, body):
       self.__store.updateCourse(id, body)
       
    #
    # course list delete
   #
   def deleteCourse(self, id):
          print '---> classroom course delete.find:'
          try:
                
                return self.__store.deleteCourse(id)
          except:
              e = sys.exc_info()[0]
              traceback.print_exc(file=sys.stdout)
              return "Error: %s" % e
     
       #
   # course list find 
   #
   def listCourse(self):
       print '---> classroom course list.find:'
       return self.__store.listCourse()

   #
   # example: find data
   #
   def find(self, name):
      print '---> classroom.find:', name
      return self.__store.find(name)

   #
   # example: add data
   #
   def add(self, name, value):
      try:
         self.__store.insert(name, value)
         self.__store.names();
         return 'success'
      except:
         return 'failed'
     
   def auth(self, email, pwd):
       print '-->in room.auth'
       return self.__store.auth(email,pwd)
   
   def addUser(self,email,pwd,fname,lname):
       print '-->in room.addUser'
       return self.__store.addUser(email,pwd,fname,lname)
   
   def updateUser(self, email, data):
       print '-->in room.updateUser'
       return self.__store.updateUser(email,data)

   def deleteUser(self, email):
       print '---> in delete user classroom..'
       return self.__store.deleteUser(email)
            
        
   def getUser(self, email):
       print '---> in get User classroom'
       return self.__store.getUser(email)
   
   def addCourse(self, body):
       print '---> in add Course classroom'
       return self.__store.addCourse(body)

   #
   # category find 
   #
   def catfind(self,id):
      print '---> classroomcategory.find:',id
      return self.__store.catfind(id)

   #
   # category list find 
   #
   def catlistfind(self):
      print '---> classroom category list.find:'
      return self.__store.catlistfind()

   #
   # Category add data
   #
   def catadd(self,catname,catdesc,catcreatedate,catstatus):
      try:
         print 'sweta: in classroom -> category add'
         print 'details:', catname
         print 'details:', catdesc
         print 'details:', catcreatedate
         print 'details:', catstatus
         
         self.__store.catinsert(catname,catdesc,catcreatedate,catstatus)
         self.__store.names();
         return 'success'
      except:
         return 'failed'

   #
   # announcement find 
   #
   def announcementfind(self,id):
      print '---> classroom.announcementfind:',id
      return self.__store.announcementfind(id)

   #
   # announcement list find 
   #
   def announcementlistfind(self):
      print '---> classroom announcement list.find:'
      return self.__store.announcementlistfind()


   #
   # announcement add data
   #
   def announcementadd(self,courseid,anntitle,anndesc,annpostdate,annstatus):
      try:
         self.__store.announcementinsert(courseid,anntitle,anndesc,annpostdate,annstatus)
         self.__store.names();
         return 'success'
      except:
         return 'failed'

         
      # TODO success|failure

   #
   # dump the configuration in the requested format. Note placing format logic
   # in the functional code is not really a good idea. However, it is here to
   # provide an example.
   #
   #
   def dump_conf(self, format):
      if format == Room.json:
         return self.__conf_as_json()
      elif format == Room.html:
         return self.__conf_as_html()
      elif format == Room.xml:
         return self.__conf_as_xml()
      elif format == Room.text:
         return self.__conf_as_text()
      else:
         return self.__conf_as_text()

   #
   # output as xml is supported through other packages. If
   # you want to add xml support look at gnosis or lxml.
   #
   def __conf_as_json(self):
      return "xml is hard"

   #
   #
   #
   def __conf_as_json(self):
      try:
         all = {}
         all["base.dir"] = self.base
         all["conf"] = self.conf
         return json.dumps(all)
      except:
         return "error: unable to return configuration"

   #
   #
   #
   def __conf_as_text(self):
      try:
        sb = StringIO.StringIO()
        sb.write("Room Configuration\n")
        sb.write("base directory = ")
        sb.write(self.base)
        sb.write("\n\n")
        sb.write("configuration:\n")
        
        for key in sorted(self.conf.iterkeys()):
           print >> sb, "%s=%s" % (key, self.conf[key])
        
        str = sb.getvalue()
        return str
      finally:
        sb.close()

#
      return "text"

   #
   #
   #
   def __conf_as_html(self):
      try:
        sb = StringIO.StringIO()
        sb.write("<html><body>")
        sb.write("<h1>")
        sb.write("Room Configuration")
        sb.write("</h1>")
        sb.write("<h2>Base Directory</h2>\n")
        sb.write(self.base)
        sb.write("\n\n")
        sb.write("<h2>Configuration</h2>\n")
        
        sb.write("<pre>")
        for key in sorted(self.conf.iterkeys()):
           print >> sb, "%s=%s" % (key, self.conf[key])
        sb.write("</pre>")
     
        sb.write("</body></html>")

        str = sb.getvalue()
        return str
      finally:
        sb.close()

#
# test and demonstrate the setup
#
if __name__ == "__main__":
  if len(sys.argv) > 2:
     base = sys.argv[1]
     conf_fn = sys.argv[2]
     svc = Room(base, conf_fn)
     svc.dump_conf()
  else:
     print "usage:", sys.argv[0], "[base_dir] [conf file]"
