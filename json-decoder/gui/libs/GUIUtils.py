from tkinter import Entry, Label, Tk, Button, StringVar, messagebox
from tkinter.constants import *
from pathlib import Path
import os,sys,traceback
path = str(os.getcwd()) + "/libs/enc"
sys.path.append(path)
from enc import encrypt, decrypt

def createUser():
	root = Tk()
	root.geometry("500x200")
	root.title("Create User")
	uname = StringVar(root)
	passwd = StringVar(root)
	Label(root, text="Username for your account").pack()
	uname_entry = Entry(root, bd=5, textvariable=uname).pack()
	Label(root, text="Account password").pack()
	passwd_entry = Entry(root, bd=5, show="*", textvariable=passwd).pack()
	def callback():
		#print(uname.get()) #Debug
		#print(passwd.get()) #Debug
		fpath = str(os.path.normpath(os.getcwd())) + "/data/unec/users.txt"
		try:
			f = open(fpath, "w+")
			f.write("Username: " + uname.get() + "\t" + "Password: " + passwd.get())
			f.flush()
			f.close()
			messagebox.showinfo("Message", "Saving User data...")
			encrypt()
			messagebox.showinfo("Message", "Done!")
		except Exception as e:
			traceback.print_exc()
			root.destroy()
			exit()
		#end
		root.destroy()
	#end
	Button(root, text="Submit", width=10, command=callback).pack()
	root.mainloop()
#end

"""def editUser():
	root = Tk()
	root.title("Edit User")
	a = decrypt()
	Label(root, text=a).pack()
	Button(root, text="OK", width=5, command=root.destroy).pack()
	#end
#end
"""
