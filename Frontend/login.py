from os import PathLike
import sys
from tkinter import *
import tkinter.messagebox as MessageBox

sys.path.insert(0, '../Todo/Database')
from DataHandler import *
from todo import todoMain

class todoLogin():
    def __init__(self):
        global root
        root = Tk()
        root.title("ToDo App Login")
        root.geometry("540x360")
        root.config(bg="#323")
        root.iconbitmap("../ToDo/Frontend/images/appLogo.ico")
        root.resizable(False, False) # not resizable in both directions

        #Validate Function
        def validate():
            username = UserEntry.get()
            password = PassEntry.get()
            dataHandlerObject = DataHandler()
            currentUser = dataHandlerObject.checkLogin(username, password)
            if currentUser != None:
                root.destroy()
                todoObject = todoMain(currentUser)

        #Labels
        TitleLabel = Label(root, text="ToDo",bg="#323" ,fg="white", font = ("Arial",23,"bold"))
        TitleLabel.place(x=220, y=50)

        UserLabel = Label(root, text="User Name : ",bg="#323", fg="white", font=("Arial",15))
        UserLabel.place(x=150, y=120)

        PassLabel = Label(root, text=" Password  : ", bg="#323", fg="white", font=("Arial",15))
        PassLabel.place(x=150, y=170)

        #EntryBox
        UserEntry = Entry(root, borderwidth=3)
        UserEntry.place(x=270, y=125)

        PassEntry = Entry(root, borderwidth=3)
        PassEntry.place(x=270, y=175)

        #Button
        Submit = Button(root, text="Login", bg="white", fg="black", font=("Arial",13), command=validate)
        Submit.place(x=245, y=240)

        root.mainloop()
