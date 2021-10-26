import json

class DataHandler:
     def __init__(self):
         pass

     def readfromDB(self):
         with open('../Todo/Database/user.txt') as f:
              data = json.load(f)         
         return data

     def writeToDB(self, database):
         with open('../Todo/Database/user.txt', 'w') as outfile:
            json.dump(database, outfile)

     def createNewUser(self,data):
         handlerObject = DataHandler()
         database = handlerObject.readfromDB()
         #print(len(database))
         database.append(data)
         handlerObject.writeToDB(database)

     def addNewTask(self ,username, newTask):
         handlerObject = DataHandler()
         database = handlerObject.readfromDB()
         for user in database :
             if user.get("username") == username :
                user.get("tasks").append(newTask)
                break
         handlerObject.writeToDB(database)    

     def removeNewTask(self ,username, oldTask):
         handlerObject = DataHandler()
         database = handlerObject.readfromDB()
         for user in database :
             if user.get("username") == username :
                user.get("tasks").remove(oldTask)
                break
         handlerObject.writeToDB(database)

     def checkLogin(self , username , password):
         newObject = DataHandler()
         database = newObject.readfromDB()
         for user in database :
             if user.get("username") == username and user.get("password") == password :
                print("Başarılı")
                return True  
                break
             else:
                print("Başarısız Giriş") 
                return False
     
                          
# Tests for Datahandler class
"""
### Add new user to DB
database = DataHandler()
data1 = {"username" : "Mert","password": "123" , "tasks":["reading book","go to the school"]}
data2 = {"username" : "Kaan","password": "abc" , "tasks":["do homework","do some exercise"]}
data3 = {"username" : "Yusuf","password": "456" , "tasks":["study English","prepare for Math exam"]}
data4 = {"username" : "Mehmet","password": "dfg" , "tasks":["go to gym","prepare for English exam"]}
for data in [data1, data2, data3, data4]:
    database.createNewUser(data)
"""

"""
### Check User in DB
database = DataHandler()
database.checkLogin("Mert", "123")
"""

"""
### Add/remove task to/from DB
database = DataHandler() 
database.addNewTask("Mert","go home")
database.removeNewTask("Yusuf","study English")
"""






