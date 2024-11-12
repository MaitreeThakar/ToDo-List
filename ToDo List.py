from tkinter import *
from tkinter.font  import Font
from tkinter import filedialog
import pickle
import tkinter


root = Tk()
root.title("todo")
root.geometry("400x650+400+100")
root.resizable(False, False)
root['bg']=  "#F6CCCB"#"#e9f094" #"#edb4f3" 

#Adding a rectangle for heading
canvas = tkinter.Canvas(root,width=500,height=70,bd=0,highlightthickness=0)
canvas.create_rectangle( 0, 20, 500,70, fill="#F6CCCB",outline="#F6CCCB")
canvas['bg']=  "#F6CCCB"
canvas.pack()

#All functions for button and menu
def add_button():
    listbox.insert(END,task_entry.get())
    task_entry.delete(0, END)
root.bind("<Return>", lambda e:add_button())
def delete_button():
    listbox.delete(ANCHOR)

def cross_button():
    try:
        listbox.itemconfig(listbox.curselection(),fg="#FFBCB6")
        listbox.selection_clear(0,END)
    except:
        pass

def uncross_button():
    try:
        listbox.itemconfig(listbox.curselection(), fg="black")
        listbox.selection_clear(0, END)
    except:
        pass



def save_list():
    file_name = filedialog.asksaveasfilename(initialdir="C:",
    title="Save file", filetypes=(("Dat files", "*.dat"), ("All Files", "*.*")))
    if file_name:
        if file_name.endswith(".dat"):
            pass
        else:
            file_name = f'{file_name}.dat'


    #Not including crossed items
    count = 0
    while count < listbox.size():
        if listbox.itemcget(count, "fg") == "black":
            listbox.delete(listbox.index(count))
        count += 1
    stuff = listbox.get(0,END)
    try:
        output_file = open(file_name,"wb")
        pickle.dump(stuff,output_file)
    except:
        pass


def open_list():
    file_menu = filedialog.askopenfilename(initialdir="C:",
                                             title="Open file", filetypes=(("Dat files", "*.dat"), ("All Files", "*.*")))
    if file_menu:
        listbox.delete(0, END)

    try:
        input_file= open(file_menu,'rb')
        stuff = pickle.load(input_file)
        for item in stuff:
            listbox.insert(END,item)
    except:
        pass
def clear_list():
    listbox.delete(0, END)

#Adding menu
my_menu = Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)

#Adding things into menu
file_menu.add_command(label="save list", command=save_list)
file_menu.add_command(label="open list", command=open_list)
file_menu.add_separator()
file_menu.add_command(label="clear list", command=clear_list)

#My fonts
my_fonts = Font(family="Segoe Print",size=15)

#Heading
heading = Label(root,text="To-Do List",font=("Forte",25),fg = "black", bg = "#F6CCCB")
heading.place(x=130 , y= 23)


#Main frame
frame = Frame(root,width=400,height= 50,bg= "#F6CCCB")
frame.place(x=0,y=100)

#Entry box in frame
task_entry = Entry(frame,font=my_fonts,bd=0,bg="#FFEBEB",width=19)
task_entry.place(x=20, y=7)
task_entry.focus()

#Add button
button = Button(frame,text="ADD",font=("Ink Free", 14,"bold"),bg="#FF5C77",fg="black",width=6,bd=0,command=add_button)
button.place(x=305, y=7)


#Second frame for listbox
frame1 = Frame(root,bd=3,width=800,height=280, bg= "#F6CCCB" ,highlightthickness=2) #"#F6CCCB"
frame1.place(x=19,y=180)

#listbox for stuff
listbox = Listbox(frame1,width=22,
                  height=6,
                  font=my_fonts,
                  bg= "#FFA39A",
                  fg="black",
                  cursor="hand2",
                  selectbackground= "#F6CCCB",
                  bd=0,
                  highlightthickness=0,
                  activestyle="none")
listbox.pack(side = LEFT,fill=BOTH, padx=2)



#Scrollbar besides listbox
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

#Button frame
button_frame = Frame(root,bg="#F6CCCB")
button_frame.pack(side=BOTTOM,pady=190)

#Adding 3 buttons in the bottom
delete_button = Button(button_frame,text="delete item",font=("Tempus Sans ITC",10,"bold"),bg="#FFEBEB",fg="black",command=delete_button)
cross_button = Button(button_frame,text="cross item",font=("Tempus Sans ITC",10,"bold"),bg="#FFEBEB",fg="black",command=cross_button)
uncross_button = Button(button_frame,text="uncross item",font=("Tempus Sans ITC",10,"bold"),bg="#FFEBEB",fg="black",command=uncross_button)

#Button grid for button spacing
delete_button.grid(row=0,column=0,padx=(14,10))
cross_button.grid(row=0,column=1)
uncross_button.grid(row=0,column=2,padx=10)



root.mainloop()
