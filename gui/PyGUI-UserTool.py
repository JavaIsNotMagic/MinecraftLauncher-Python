from tkinter import Tk, Button, messagebox
from tkinter.constants import *
import os,sys
path = str(os.getcwd()) + "/libs"
sys.path.append(path)
from GUIUtils import createUser,editUser
#main
def about():
	text = "Connor for the original idea and creation of the multiple GUI's.\n\nCaleb for his imense Python knowledege and debugging skills."
	messagebox.showinfo("HaxiumLauncher Credits", text)
#end
def do_nothing():
	pass
#end

tk = Tk()
tk.title("HaxiumLauncher User Tools")
tk.geometry("500x200")
Button(tk, text="Create User", width=15, command=createUser).pack()
Button(tk, text="Edit User", width=15, command=editUser).pack()
Button(tk, text="Delete User", width=15, command=do_nothing).pack()
Button(tk, text="Exit", width=5, command=tk.destroy).pack()
tk.mainloop()