from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import os
import sys
import pickle


# To import our modules
sys.path.insert(0, '../Todo/Database')
from DataHandler import *

class todoMain():
    def __init__(self, currentUser):
        database = DataHandler()    
        self.currentUser = currentUser          
        #crate app window, set title, logo and size
        global root
        root = Tk()
        root.title('7.Tepe-Dev Python To-Do List App')
        root.iconbitmap('../ToDo/Frontend/images/appLogo.ico')
        root.geometry("640x480")
        root.config(bg="#323")
        root.resizable(False, False) # not resizable in both directions

        #default font
        my_font = Font (
            family = "Arial",
            size = 16,
            weight = "normal",
            slant = "roman",
            underline = 0,
            overstrike = 0
        )

        #create a frame inside app window
        my_frame = Frame(root)
        my_frame.pack(pady=10)

        #create todo list box
        my_list = Listbox(my_frame,
            font=my_font,
            width=50,
            height=10,
            bg = "SystemButtonFace", #make background colorless
            bd = 0, #remove list border
            fg= "#202124", #font color
            highlightthickness=0, #removes listbox border
            selectbackground="#555", #focus bg
            activestyle="none" #remove underline
        )

        my_list.pack(side=LEFT, fill=BOTH)

        #temporary list
        stuff = self.currentUser.get("tasks")
        # # add temp list to listbox
        for item in stuff:
            my_list.insert(END, item)

        #create scrollbar
        my_scrollbar = Scrollbar(my_frame)
        my_scrollbar.pack(side=RIGHT, fill=BOTH)

        # add scrollbar
        my_list.config(yscrollcommand=my_scrollbar.set)
        my_scrollbar.config(command=my_list.yview)

        #entry box to add items
        my_entry = Entry(root, font=("Arial", 16), width=42)
        my_entry.pack(pady=30)

        #create button frame
        button_frame = Frame(root, bg="#323")
        button_frame.pack(pady=20)

        # create command functions
        def delete_item():
            my_list.delete(ANCHOR) # deletes the highlighted item

        def add_item():
            my_list.insert(END, my_entry.get()) # gets data from box and inserts it to the end of the list
            database.addNewTask(self.currentUser.get("username"), my_entry.get())
            my_entry.delete(0, END) # after inserting new item, empty the entry box


        def cross_off_item(): # cross off item, but we cant really use cross, just lighten the color
            my_list.itemconfig(
                my_list.curselection(),
                fg="#bcbcbc"
            )
            # remove highlight bar when cross off item
            my_list.select_clear(0, END)

        def uncross_item():
            my_list.itemconfig(
                my_list.curselection(),
                fg="#202124"
            )
            # remove highlight bar when cross off item
            my_list.select_clear(0, END)

        def delete_crossed():
            # print(my_list.size())
            count = 0
            while count<my_list.size():
                if my_list.itemcget(count, "fg") == "#bcbcbc":
                    my_list.delete(my_list.index(count))
                else:
                    count+=1

        # print(os.getlogin())
        # print(os.getenv('username'))

        path = ''.join(('C:/Users/', os.getenv('username'), '/Desktop/'))

        def save_list():
            file_name = filedialog.asksaveasfilename(
                initialdir=path,
                title="Save File",
                filetypes=(
                    ("Dat Files", "*.dat"),
                    ("Json Files", "*.json"),
                    ("All Files", "*.*")
                )
            )
            if file_name:
                if file_name.endswith(".dat"):
                    pass
                else:
                    file_name = f'{file_name}.dat'

                # delete crossed items when saving to a file
                count = 0
                while count<my_list.size():
                    if my_list.itemcget(count, "fg") == "#bcbcbc":
                        my_list.delete(my_list.index(count))
                    else:
                        count+=1

                # grab all items from the list
                stuff = my_list.get(0, END)

                # open file
                output_file = open(file_name, 'wb')

                # add items to the file
                pickle.dump(stuff, output_file)

        def open_list():
            file_name = filedialog.askopenfilename(
                initialdir=path,
                title="Open File",
                filetypes=(
                    ("Dat Files", "*.dat"),
                    ("Json Files", "*.json"),
                    ("All Files", "*.*")
                )
            )

            if file_name:
                # delete the currently open list
                my_list.delete(0, END)

                # open the file
                input_file = open(file_name, 'rb')

                # load data from file
                stuff = pickle.load(input_file)

                # output items to the screen

                for item in stuff:
                    my_list.insert(END, item)

        def clear_list():
            my_list.delete(0, END)

        # add buttons
        add_button = Button(button_frame, text="Add Item", command=add_item)
        delete_button = Button(button_frame, text="Delete Item", command=delete_item)
        cross_off_button = Button(button_frame, text="Cross Off Item", command=cross_off_item)
        uncross_button = Button(button_frame, text="Uncross Item", command=uncross_item)

        delete_crossed_button = Button(button_frame, text="Delete Crossed Items", command=delete_crossed)

        save_list_button = Button(button_frame, text="Save This ToDo", command=save_list)
        open_list_button = Button(button_frame, text="Open a ToDo List", command=open_list)
        clear_list_button = Button(button_frame, text="Clear This ToDo", command=clear_list)

        # grid the buttons, only 1 row with all buttons
        add_button.grid(row=0, column=0)
        delete_button.grid(row=0, column=1,padx=20)
        cross_off_button.grid(row=0, column=2)
        uncross_button.grid(row=0, column=3, padx=20)
        delete_crossed_button.grid(row=0, column=4)

        save_list_button.grid(row=1, column=0, pady=10)
        open_list_button.grid(row=1, column=1, padx=20)
        clear_list_button.grid(row=1, column=4)

        root.mainloop()

# todoMainObject = todoMain("")