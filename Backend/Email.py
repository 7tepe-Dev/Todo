import smtplib
from email.mime.text import MIMEText

class Email:
    def __init__(self):
        self.host = "smtp.gmail.com"
        self.port = 465           #587
        self.username = "kaanto77@gmail.com"
        self.password = "11111"
        self.sender = "kaanto77@gmail.com"
        self.targets = ["ekerdiker.yusuf@gmail.com"]

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

email = Email()
email.setEmail("Hacklendinizzzz!!!!!")
email.sendEmail()