import smtplib
from email.mime.text import MIMEText

class Email:
    def __init__(self, target):
        self.host = "smtp.gmail.com"
        self.port = 465           #587
        self.username = "ekerdiker18@gmail.com"
        self.password = "BURAYA PASSWORD YAZINIZ"
        self.sender = "ekerdiker18@gmail.com"
        self.targets = [target]

    def setEmail(self, userTasks):
        self.msg = MIMEText("{}".format(userTasks))
        self.msg['Subject'] = 'Hello'
        self.msg['From'] = self.sender
        self.msg['To'] = ', '.join(self.targets)
        
    def sendEmail(self):
        server = smtplib.SMTP_SSL(self.host, self.port)
        server.login(self.username, self.password)
        server.sendmail(self.sender, self.targets, self.msg.as_string())
        server.quit()
