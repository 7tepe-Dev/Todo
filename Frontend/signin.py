from os import PathLike
import sys
from tkinter import *
import tkinter.messagebox as MessageBox

import Database.dataHandler as db
# from todo import todoMain
# from login import todoLogin
import Backend.user as usr
import Frontend.todo as td
import Frontend.login as log
class todoSignin():
    def __init__(self):
        global root
        root = Tk()
        root.title("ToDo App Sign in")
        root.geometry("540x360")
        root.config(bg="#323")
        root.iconbitmap("../ToDo/Frontend/images/appLogo.ico")
        root.resizable(False, False) # not resizable in both directions

        #Validate Function
        def validate():
            username = UserEntry.get()
            password = PassEntry.get()
            email = EmailEntry.get()
            tasks = []
            dataHandlerObject = db.DataHandler()
            newUser = usr.User(username, password, email, tasks)
            currentUser = dataHandlerObject.checkLogin(username, password)
            if currentUser != None:
                root.destroy()
                todoObject = td.todoMain(currentUser)

        def loginRedirect():
            root.destroy()
            loginObject = log.todoLogin()

        #Labels
        TitleLabel = Label(root, text="ToDo",bg="#323" ,fg="white", font = ("Arial",23,"bold"))
        TitleLabel.place(x=220, y=50)

        UserLabel = Label(root, text="User Name : ",bg="#323", fg="white", font=("Arial",15))
        UserLabel.place(x=150, y=120)

        PassLabel = Label(root, text=" Password  : ", bg="#323", fg="white", font=("Arial",15))
        PassLabel.place(x=150, y=170)

        EmailLabel = Label(root, text=" Email  : ", bg="#323", fg="white", font=("Arial",15))
        EmailLabel.place(x=150, y=220)

        #EntryBox
        UserEntry = Entry(root, borderwidth=3)
        UserEntry.place(x=270, y=125)

        PassEntry = Entry(root, borderwidth=3)
        PassEntry.place(x=270, y=175)

        EmailEntry = Entry(root, borderwidth=3)
        EmailEntry.place(x=270, y=225)

        #Button
        Submit = Button(root, text="Sign in", bg="white", fg="black", font=("Arial",13), command=validate)
        Submit.place(x=205, y=290)

        Submit = Button(root, text="Login", bg="white", fg="black", font=("Arial",13), command=loginRedirect)
        Submit.place(x=245, y=290)

        root.mainloop()
