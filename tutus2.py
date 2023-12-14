from tkinter import *

root = Tk()
root.title("PHARMANCY MANAGENMENT SYSYTEM ")
root.geometry("600x600")
# Creating a Label widget to display text on the window 
Title_label = Label(text="PHARMANCY MANAGENMENT SYSTEM ",bg = "red",fg="white",relief=SUNKEN, font=('Poppins bold', 19))
Title_label.pack(fill=BOTH)
content_label = Label(root,text="login",bg="grey",fg="white",font=("poppins bold",27),relief=RAISED)
content_label.pack()
frame= Frame(root, relief= 'sunken', bg= "grey")
frame.pack(fill= BOTH, expand= True, padx= 10, pady=20)
root.mainloop()