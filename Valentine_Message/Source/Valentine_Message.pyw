#--------------------

name = ""

#--------------------

from tkinter import messagebox
if name=="": message="Will you be my Valentine ?" 
else: message="Will you be my Valentine, "+name+" ?"
if messagebox.askquestion(title=None,message=message)=="yes": messagebox.showinfo(title=None,message="Yay !") 
else: messagebox.showerror(title=None,message=":(")