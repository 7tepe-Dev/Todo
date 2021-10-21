from ssl import SSL_ERROR_INVALID_ERROR_CODE


class User:
    def __init__(self, username, password, usertasks):
        self.username = username
        self.passsword = password
        self.usertasks = usertasks
        userData = {"username":self.username, "password":self.passsword, "usertasks":self.usertasks}
        

    def getUserName(self):
        return self.username
    def getPassword(self):
        return self.passsword
    def getUserTasks(self):
        return self.usertasks            
    
    def addTask(self, newTask):
        self.usertasks.append(newTask)
    def removeTask(self, oldTask):
        self.usertasks.remove(oldTask)


User1 = User("Kaan", "1234", ["Kitap oku"])
User2 = User("Mert", "0000", ["Markete git"])
User3 = User("Yusuf", "1212", ["Ders çalış"])

print(User1.getUserName())
print(User1.getPassword())
print(User1.getUserTasks())

User1.addTask("Okula git")
User1.removeTask("Kitap oku")
print(User1.getUserTasks())