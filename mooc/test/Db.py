from pymongo import Connection

connection= Connection()
db=connection['cmpe275-project2']
names=db.names
name= {'name': 'pritish'}
names.insert(name)
print db.names.find()
