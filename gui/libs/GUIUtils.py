from tkinter import Entry, Label, Tk, Button, StringVar, messagebox
from tkinter.constants import *
from uuid import uuid4
from pathlib import Path
import os

data_dir = str(os.getcwd()) + "/data"
def createUser():
	root = Tk()
	root.geometry("500x200")
	root.title("Create User")
	uname = StringVar()
	passwd = StringVar()
	Label(root, text="Username").pack()
	uname_entry = Entry(root, bd=5, textvariable=uname).pack()
	Label(root, text="Password").pack()
	passwd_entry = Entry(root, bd=5, show="*", textvariable=passwd).pack()
	def callback():
		#print(uname.get()) #Debug
		#print(passwd.get()) #Debug
		messagebox.showinfo("User Creator", "All set!")
	#end
	Button(root, text="Submit", width=10, command=callback).pack()
	Button(root, text="Done", width=5, command=root.destroy).pack()
	root.mainloop()
#end