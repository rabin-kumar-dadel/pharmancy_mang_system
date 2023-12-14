from tkinter import *
root = Tk()
root.geometry("600x600")
class pharmancymanagenment():
    def __init__(self,root):
        self.root = root
        self.root.title(" welcome to pharmancy managenment system")

    def Content_label(self):
        lbl=Label(self.root,text="This is a PharmaCY Management System",font=('arial',25,' bold'),bg='lightgreen')
        lbl.pack(pady=10)
if __name__ == "__main__":
    obj = pharmancymanagenment(root)
    obj.Content_label()
    root.mainloop()    



    