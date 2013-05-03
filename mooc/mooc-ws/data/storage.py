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
    # def for sign in
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
                    #response.status = 
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
            c = db.discussioncollection.find(st)
            print c.count()
            if c.count() > 0:
                try:
                    db.discussioncollection.remove(st)
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
            c = db.announcementcollection.find(st)
            print c.count()
            if c.count() > 0:
                try:
                    db.announcementcollection.remove(st)
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
                db.discussioncollection.update(st, {'$set': body})
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
                db.annoucementcollection.update(st, {'$set': body})
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
      print "---> storage.getCourse:", id
      connection = Connection()
      db = connection['cmpe275']
      c = db.coursecollection.find({"_Id":id}).count()
      print "Count-->", c
      st = {"_Id":id}
      print "String-->", st
      courseDetails = db.coursecollection.find(st)
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
        connection = Connection()
        db = connection['cmpe275']
        c = db.coursecollection.find().count()
        print "Count-->", c
        courseList = db.coursecollection.find()
        print courseList.count()
        lst = []
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
            email = rowset1[0]['email']
            result = db.usercollection.update({'email':email}, {'$pull':{'own':id}})
            
            rowset2 = db.usercollection.find({'enrolled':{'$all':[id]}})
            for r in rowset2:
                tempEmail = r['email']
                print tempEmail
                db.usercollection.update({'email':tempEmail}, {'$pull':{'enrolled':id}})
                
                st = {"_Id":id}
                c = db.coursecollection.find(st)
                print c.count()
                if c.count() > 0:
                    try:
                        db.coursecollection.remove(st)
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
                db.coursecollection.update(st, {'$set': body})
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
                 response.status = 500
                 return {'msg': 'Data not added'}
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
             #print db.usercollection.update(st,{ '$set' : body })
             #for key,value in body:    #to add old password new password func.
                #data = json.loads(key)
             #oldpassword = db.usercollection.find(st,{'pwd':pwd})
             #if data["oldpassword"] == oldpassword["pwd"]:
                 #body = {'pwd': data['newpassword'], 'fName': data['fName'], 'lName': data['lName'] }
                
                 db.usercollection.update(st,{ '$set' : body })
                 print "Updateddd"
                 msg = {"msg":'Existing User Updateddd'}
                 response.status = 200
                 return msg
             
         else:
             print "No User Found. It will create new User."
             for key,value in body:
                data = json.loads(key)
             msg = Storage.addUser(self, data['email'], data['newpassword'], data['fName'], data['lName'])
             response.status = 201  
             #msg = {"msg":'User Not Updateddd'}
             return msg
    
    
    #delete User 
    def deleteUser(self, email):
        connection = Connection()
        db = connection['cmpe275']
        c = db.usercollection.find({"email":email}).count()
        if c > 0:
            st = {"email":email}
            db.usercollection.remove(st)
            response.status = 200
            return {'msg':'Delete Success'}     #what about dependencies?? also log out n go to login page.
        elif c == 0:
             response.status = 404
             return {'msg': 'Email not found'}
        else:
            response.status = 400
            return {'msg': 'Bad Request. Please try again Later..'}
             
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
        
    def getUser(self, email):
        connection = Connection()
        db = connection['cmpe275']
        c = db.usercollection.find({"email":email}).count()
        if c > 0:
            st = {"email":email}
            records = db.usercollection.find(st)
            for record in records:
                del record["_id"]
                json.dumps(record)
                print "Record:", record
                response.status = 200
                return record
        else:
            response.status = 404
            return {'msg': 'No record found. Invalid Email Id'}
        
        '''
        if email <= 0:
            response.status = 400
            return {'msg': 'please insert email id. Bad Request'}   #what if other client do not provide validations
        '''
     
    def addCourse(self, body):
        # just run below query one time
        # db.coursecollection.ensureIndex( { "courseId": 1 }, { unique: true } )
        connection = Connection()
        db = connection['cmpe275']
        count = db.coursecollection.find().count()
        courseId = count + 1
        try:
            print body
            for key, value in body:
                data = json.loads(key)
            print 'Description from storage:' + data['Description']
            #data['Description'] = "new course"
            print data
            db.coursecollection.insert({ '$set' : data })
        except:
            return {'msg': 'data not added'}


    def catfind(self, id):
      print "---> storage.find:", id
      connection = Connection()
      db = connection['cmpe275']
      c = db.categorycollection.find({"categoryId":id}).count()
      print "Count-->", c
      st = {"categoryId":id}
      print "String-->", st
      name1 = db.categorycollection.find(st)
      print name1.count()
      for record in name1:
         print "--> Inside Cursor"
         del record["_id"]
         json.dumps(record)
         print "Record:", record
      if c > 0:
          try:
              response.status = 200
              print "Get category Success"
              return record
          except:
              response.status = 500
              print "Failed in getting category", sys.exc_info()
              msg = {'msg':'Get category unsuccessful'}
              return msg                    
      else:
          try:
              response.status = 404
              msg = {'msg':'category ID not found'}
              return msg
          except:
              response.status = 400
              msg = {'msg':'category ID invaild'}
              return msg
     
    def catlistfind(self):
      print "---> storage category list.find:"
      connection = Connection()
      db = connection['cmpe275']
      c = db.categorycollection.find().count()
      print "Count-->", c
      name1 = db.categorycollection.find()
      print name1.count()
      lst = []
      for record in name1:
         print "--> Inside Cursor"
         del record["_id"]
         lst.append(record)
         print "Record:", record
     
      if c > 0:
            try:
                response.status = 200
                print "List category Success"
                return json.dumps(lst)
            except:
                response.status = 500
                print "Failed in listing category", sys.exc_info()
                msg = {'msg':'List category unsuccessful'}
                return msg
      else:
            response.status = 500
            print "Failed in listing category", sys.exc_info()
            msg = {'msg':'List category unsuccessful'}
            return msg
     
    def announcementfind(self, id):
      print "---> announcement.find:", id
      connection = Connection()
      db = connection['cmpe275']
      c = db.announcementcollection.find({"announceId":id}).count()
      print "Count-->", c
      st = {"announceId":id}
      print "String-->", st
      name1 = db.announcementcollection.find(st)
      print name1.count()
      for record in name1:
         print "--> Inside Cursor"
         del record["_id"]
         json.dumps(record)
         print "Record:", record
      if c > 0:
          try:
              response.status = 200
              print "Get announcement Success"
              return record
          except:
              response.status = 500
              print "Failed in getting announcement", sys.exc_info()
              msg = {'msg':'Get announcement unsuccessful'}
              return msg                    
      else:
          try:
              response.status = 404
              msg = {'msg':'annoncement ID not found'}
              return msg
          except:
              response.status = 400
              msg = {'msg':'announcement ID invaild'}
              return msg
     
    def announcementlistfind(self):
      print "---> storage announcement list.find:"
      connection = Connection()
      db = connection['cmpe275']
      c = db.announcementcollection.find().count()
      print "Count-->", c
      name1 = db.announcementcollection.find()
      print name1.count()
      lst = []
      for record in name1:
         print "--> Inside Cursor"
         del record["_id"]
         lst.append(record)
         print "Record:", record
      
      if c > 0:
            try:
                response.status = 200
                print "List announcement Success"
                return json.dumps(lst)
            except:
                 response.status = 500
                 print "Failed in listing announcement", sys.exc_info()
                 msg = {'msg':'List announcement unsuccessful'}
                 return msg
      else:
            response.status = 500
            print "Failed in listing announcement", sys.exc_info()
            msg = {'msg':'List announcement unsuccessful'}
            return msg
     
    def announcementinsert(self, courseid, anntitle, anndesc, annpostdate, annstatus):
        connection = Connection()
        db = connection['cmpe275']
      
        try:
          print "now herennnnnnnnnn"
          announcementcollection = db['announcementcollection']
         
          count = db.announcementcollection.find().count()
          print "count is", count
          newCount = count + 1
          
          print "new count is:", newCount
          newid = "Pinnacleannouncement_" + str(newCount)
          
          print "final id is", newid
          
          announcement = {"announceId":newid, "courseId": courseid, "title": anntitle, "description": anndesc, "postDate": annpostdate, "status": annstatus}
          announcementcollection.insert(announcement)
          print "Successfully added"
          msg = {'msg':'Successfully added'}
          response.status = 201
          return msg
        except:
            response.status = 500
            msg = {'msg':'Insert announcement unsuccessful'}
            return msg
             
        
     
def catinsert(self, catname, catdesc, catcreatedate, catstatus):
    connection = Connection()
    db = connection['cmpe275']
    c = db.usercollection.find({"name": catname}).count()
    print c
    if c == 0:
        try:
            categorycollection = db['categorycollection']
            count = db.categorycollection.find().count()
            print "count is", count
            newCount = count + 1
            print "new count is:", newCount
            newid = "Pinnaclecategory_" + str(newCount)
            print "final id is", newid
            category = {"id":newid, "name": catname, "description": catdesc, "createDate": catcreatedate, "status": catstatus}
            categorycollection.insert(category)
            print "Successfully added"
            msg = {'msg':'Successfully added'}
            response.status = 201
            return msg
        except:
            msg = {'msg':'Insert category unsuccessful'}
            response.status = 500
            return msg

    else:
         response.status = 409
         print "category already exists"
         msg = {'msg':'Category already exists'}
         return msg




