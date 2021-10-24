from tkinter import *
from tkinter.font import Font

#crate app window, set title, logo and size
root = Tk()
root.title('7.Tepe-Dev Python To-Do List App')
root.iconbitmap('./images/appLogo.ico')
root.geometry("640x480")

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
stuff = ["walk the dog", "buy groceries", "go to school", "bla bla bla"]
# add temp list to listbox
for item in stuff:
    my_list.insert(END, item)

#create scrollbar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)

# add scrollbar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

#entry box to add items
my_entry = Entry(root, font=("Arial", 12))
my_entry.pack(pady=20)

#create button frame
button_frame = Frame(root)
button_frame.pack(pady=50)

# create command functions
def delete_item():
    my_list.delete(ANCHOR) # deletes the highlighted item

def add_item():
    my_list.insert(END, my_entry.get()) # gets data from box and inserts it
                                        # to the end of the list
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
    count = 0
    while count<my_list.size():
        if my_list.itemcget(count, "fg") == "bcbcbc":
            my_list.delete(my_list.index(count))
        count+=1

# add buttons
delete_button = Button(button_frame, text="Delete Item", command=delete_item)
add_button = Button(button_frame, text="Add Item", command=add_item)
cross_off_button = Button(button_frame, text="Cross Off Item", command=cross_off_item)
uncross_button = Button(button_frame, text="Uncross Item", command=uncross_item)

delete_crossed_button = Button(button_frame, text="Delete Crossed Items", command=delete_crossed)

# grid the buttons, only 1 row with all buttons
delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1,padx=20)
cross_off_button.grid(row=0, column=2)
uncross_button.grid(row=0, column=3, padx=20)
delete_crossed_button.grid(row=0, column=4)

root.mainloop()