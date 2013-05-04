"""
Storage interface
"""

import time
from pymongo import Connection
from bson import json_util
import json
import bottle
from bottle import response, Response


class Storage(object):
 
    def __init__(self):
      # initialize our storage, data is a placeholder
      self.data = {}
      # for demo
      self.data['created'] = time.ctime()
    '''  
    def insert(self, name, value):
      connection = Connection()
      db = connection['cmpe275']
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
      db = connection['cmpe275']
      c = db.users.find({"username":'john'}).count()
      print "Count-->", c
      st = {"username":name}
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
     '''
    #def for sign in
    def auth(self, email, pwd):
        
        print "---> storage.find:", email
        connection = Connection()
        db = connection['cmpe275']
        c = db.usercollection.find({"email": email}).count()
        if c == 1:
            st = {"email":email}
            name1 = db.usercollection.find(st)
            for record in name1:
                print "--> Inside Cursor"
                del record["_id"]
                strPwd = record["pwd"]
                print pwd
                print strPwd
                if strPwd == pwd:
                    print "Login Successfull"
                    msg = {'msg':'Login Successful'}
                    return msg
                else:
                    response.status = 401
                    print "Password Incorrect"
                    msg = {'msg':'Password Incorrect'}
                    return msg           
        else:
            response.status = 401
            msg = {'msg':'Login Failed - Email not found'}
            print msg
            return msg  
        
    def deleteDiscussion(self, id):
            connection = Connection()
            db = connection['cmpe275']
            
            print id                       
                         
            st = {"_Id":id}
            c =   db.discussioncollection.find(st)
            print c.count()
            if c.count() > 0:
                try:
                    db.discussionCollection.remove(st)
                    response.status = 200
                    print "Delete discussion Success"
                    msg = {'msg':'Delete discussion Successful'}
                    return msg                    
                except:
                     response.status = 500
                     print "Failed in deleting discussion", sys.exc_info()
                     msg = {'msg':'Delete discussion unsuccessful'}
                     return msg
            else:
                try:
                    response.status = 404
                    msg = {'msg':'discussion ID not found'}
                    return msg
                except:
                    response.status = 400
                    msg = {'msg':'discussion ID invaild'}
                    return msg
            
        
    def deleteAnnouncement(self, id):
            connection = Connection()
            db = connection['cmpe275']
            
            print id                       
                         
            st = {"_Id":id}
            c =   db.announcementcollection.find(st)
            print c.count()
            if c.count() > 0:
                try:
                    db.announcementCollection.remove(st)
                    response.status = 200
                    print "Delete announcement Success"
                    msg = {'msg':'Delete announcement Successful'}
                    return msg
                except:
                     response.status = 500
                     print "Failed in deleting announcement", sys.exc_info()
                     msg = {'msg':'Delete announcement unsuccessful'}
                     return msg                    
            else:
                try:
                    response.status = 404
                    msg = {'msg':'announcement ID not found'}
                    return msg
                except:
                    response.status = 400
                    msg = {'msg':'announcement ID invaild'}
                    return msg
                    
                
                                          
                      
    def updateDiscussion(self, id, body):
        connection = Connection()
        db = connection['cmpe275']
        st = {"_Id":id}
        c = db.discussioncollection.find(st).count()
        if c > 0:
            try:
                db.discussioncollection.update(st,{'$set': body})
                response.status = 200
                print "Delete announcement Success"
                msg = {'msg':'Update discussion Successful'}
                return msg
            except:
                 response.status = 500
                 print "Failed in updating discussion", sys.exc_info()
                 msg = {'msg':'Update discussion  unsuccessful'}
                 return msg                    
        else:
            try:
                response.status = 404
                msg = {'msg':'Discussion ID not found'}
                return msg
            except:
                response.status = 400
                msg = {'msg':'Discussion ID invaild'}
                return msg
        
        
     
    def updateAnnoucement(self, id, body):
        connection = Connection()
        db = connection['cmpe275']
        st = {"_Id":id}
        c = db.annoucementcollection.find(st).count()
        if c > 0:
            try:
                db.annoucementcollection.update(st,{'$set': body})
                response.status = 200
                print "Delete announcement Success"
                msg = {'msg':'Update announcement Successful'}
                return msg
            except:
                 response.status = 500
                 print "Failed in updating announcement", sys.exc_info()
                 msg = {'msg':'Update announcement unsuccessful'}
                 return msg                    
        else:
            try:
                response.status = 404
                msg = {'msg':'announcement ID not found'}
                return msg
            except:
                response.status = 400
                msg = {'msg':'announcement ID invaild'}
                return msg
           
        
    def getCourse(self, id):
      print "---> storage.getCourse:",id
      connection=Connection()
      db=connection['cmpe275']
      c=db.coursecollection.find({"_Id":id}).count()
      print "Count-->",c
      st={"_Id":id}
      print "String-->",st
      courseDetails=db.coursecollection.find(st)
      print courseDetails.count()
      singleCourse = None
      for record in courseDetails:
         print "--> Inside Cursor"
         del record["_id"]
         json.dumps(record)
         print "Record:", record
         singleCourse = record
      if c > 0:
          try:
              response.status = 200
              print "Get course Success"
              return singleCourse
          except:
              response.status = 500
              print "Failed in getting course", sys.exc_info()
              msg = {'msg':'Get course unsuccessful'}
              return msg                    
      else:
          try:
              response.status = 404
              msg = {'msg':'course ID not found'}
              return msg
          except:
              response.status = 400
              msg = {'msg':'course ID invaild'}
              return msg
     
     # Course list find 
    def listCourse(self):
        print "---> storage category listCourse.find:"
        connection=Connection()
        db=connection['cmpe275']
        c=db.coursecollection.find().count()
        print "Count-->",c
        courseList=db.coursecollection.find()
        print courseList.count()
        lst=[]
        for record in courseList:
            print "--> Inside Cursor"
            del record["_id"]
            lst.append(record)
            print "Record:", record
        if c > 0:
            try:
                response.status = 200
                print "List course Success"
                return json.dumps(lst)
            except:
                 print "Failed in listing course", sys.exc_info()
                 msg = {'msg':'List course unsuccessful'}
                 return msg
                        
        else:
            print "Failed in listing course", sys.exc_info()
            msg = {'msg':'List course unsuccessful'}
            return msg
 
    def deleteCourse(self, id):
            connection = Connection()
            db = connection['cmpe275']
            
            print id
                           
            rowset1 = db.usercollection.find({'own':{'$all':[id]}})
            email =  rowset1[0]['email']
            result = db.usercollection.update({'email':email},{'$pull':{'own':id}})
            
            rowset2 = db.usercollection.find({'enrolled':{'$all':[id]}})
            for r in rowset2:
                tempEmail = r['email']
                print tempEmail
                db.usercollection.update({'email':tempEmail},{'$pull':{'enrolled':id}})
                
                st = {"_Id":id}
                c =   db.coursecollection.find(st)
                print c.count()
                if c.count() > 0:
                    try:
                        db.courseCollection.remove(st)
                        response.status = 200
                        print "Delete course Success"
                        msg = {'msg':'Delete course Successful'}
                        return msg
                    except:
                     response.status = 500
                     print "Failed in deleting course", sys.exc_info()
                     msg = {'msg':'Delete course unsuccessful'}
                     return msg
                    
            else:
                try:
                    response.status = 404
                    msg = {'msg':'course ID not found'}
                    return msg
                except:
                    response.status = 400
                    msg = {'msg':'course ID invaild'}
                    return msg

    def updateCourse(self, id, body):
        connection = Connection()
        db = connection['cmpe275']
        st = {"_Id":id}
        c = db.coursecollection.find(st).count()
        if c > 0:
            try:
                db.coursecollection.update(st,{'$set': body})
                response.status = 200
                print "Delete announcement Success"
                msg = {'msg':'Update course Successful'}
                return msg
            except:
                 response.status = 500
                 print "Failed in updating course", sys.exc_info()
                 msg = {'msg':'Update course unsuccessful'}
                 return msg
                    
        else:
            try:
                response.status = 404
                msg = {'msg':'course ID not found'}
                return msg
            except:
                response.status = 400
                msg = {'msg':'course ID invaild'}
                return msg
           

    #def for Create User
    def addUser(self,name,value,fname,lname):
             connection=Connection()
             db=connection['cmpe275']
             c=db.usercollection.find({"email": name}).count()
             print c
             if c == 0:
                 try:
                     user={"email": name, "pwd": value , "fname": fname, "lname": lname}
                     usercollection=db['usercollection']
                     usercollection.insert(user)
                     print "Successfully added"
                     msg = {'msg':'Successfully added'}
                     response.status = 201
                     return msg  
                 except:
                     return "error: data not added"
             else:
                 response.status = 409
                 print "Email already exists"
                 msg = {'msg':'Email already exists'}
                 return msg 
    
    #Update User
    def updateUser(self, email, body):
             connection = Connection()
             db = connection['cmpe275']
             st = {"email":email}
             c = db.usercollection.find(st).count()
             print "Updateddd st " , st
             print "Updateddd c" , c
             print "Updateddd body" , body
             
             if c > 0:
                 print db.usercollection.update(st,{ '$set' : body })
                 db.usercollection.update(st,{ '$set' : body })
                 print "Updateddd"
                 msg = {"msg":'User Updateddd'}
                 return msg
             else:
                 print "Nottt Updateddd"
                 msg = {"msg":'User Not Updateddd'}
                 return msg
    
    
        #delete User 
    def deleteUser(self, email):
            connection = Connection()
            db = connection['cmpe275']
            c = db.usercollection.find({"username":email}).count()
            if c > 0:
                st = {"username":email}
                db.usercollection.remove(st)
                return 'delete Success'
            else:
                 return 'email not found'
             
    def getUser(self, email):
        connection = Connection()
        db = connection['cmpe275']
        c = db.usercollection.find({"username":email}).count()
        if c > 0:
            st = {"username":email}
            records = db.usercollection.find(st)
            for record in records:
                del record["_id"]
                json.dumps(record)
                print "Record:", record
        else:
            return "No record found. Invalid Email Id"
        
        if email > 0:
            return record
        else:
            return None
     
    def addCourse(self, body):
      #just run below query one time
      #db.coursecollection.ensureIndex( { "courseId": 1 }, { unique: true } )
        connection = Connection()
        db = connection['cmpe275']
        count = db.coursecollection.find().count()
        courseId = count + 1
        try:
            print body
            for key, value in body:
                data = json.loads(key)
            print 'Description from storage:' + data['Description']
            data['Description'] = "new course"
            print data
          #db.coursecollection
          
          #db.coursecollection.insert({ '$set' : data })
        except:
            return "error: data not added"





