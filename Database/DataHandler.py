import json
class DataHandler:
     def __init__(self):

         pass

     def readfromDB(self):
         database = ""
         with open('user.txt') as f:
              data = json.load(f)

            
         return data
         pass

     def createNewUser(self,data):
         newObject = DataHandler()
         database = newObject.readfromDB()
         database.append(data)

         with open('user.txt', 'w') as outfile:
            json.dump(database, outfile)

     def addNewTask(self ,username, newTask):
         newObject = DataHandler()
         database = newObject.readfromDB()
         for user in database :
             if user.get("username") == username :
                user.get("task").append(newTask)
                break

         with open('user.txt', 'w') as outfile:
            json.dump(database, outfile)    

     def removeNewTask(self ,username, oldTask):
         newObject = DataHandler()
         database = newObject.readfromDB()
         for user in database :
             if user.get("username") == username :
                user.get("task").remove(oldTask)
                break

         with open('user.txt', 'w') as outfile:
            json.dump(database, outfile)
                
             
         


           
         


     def checkLogin(self , username , password):
         newObject = DataHandler()
         database = newObject.readfromDB()
         for user in database :
             if user.get("username") == username and user.get("password") == password :
                print("Başarılı")  
                break
             else:
                print("Başarısız Giriş") 
     
                
                   
           

database = DataHandler()

"""
data1 = {"username" : "Mert","password": "123" , "tasks":["reading book","go to the school"]}
data2 = {"username" : "Kaan","password": "abc" , "tasks":["do homework","do some exercise"]}
data3 = {"username" : "Yusuf","password": "456" , "tasks":["study English","prepare for Math exam"]}
allData = []
allData.append(data1)
allData.append(data2)
allData.append(data3)


database.writetoDB(allData)


database.checkLogin("Mert", "123")


data4 = {"username" : "Mehmet","password": "dfg" , "tasks":["go to gym","prepare for English exam"]}

database.createNewUser(data4)
"""
database.addNewTask("Mert","go home")
database.removeNewTask("Yusuf","study English")






