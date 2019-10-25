import gi,os
#Other Imports
path = os.getcwd()
file = path + "/data/" + "database.db"
text = None
text1 = None
#GUI
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
#User Creation
#Following: https://stackoverflow.com/questions/37837682/python-class-input-argument/37837766
class new_user_handler(obj):
	global text
	global text1
	def __init__(builder_obj):
		print("Hello World!")
		new_user_object = self.builder_obj
	#end
	def new_user_close(self, *args):
		print("Close window")
		Gtk.main_quit()
	#end
	def new_user_uname(self, *args):
		print("Grabbed username")
		entry = new_user_builder.get_object('new_user_uname')
		text = entry.get_text()
	#end
	def new_user_password(self, *args):
		print("Grabbed password")
		entry1 = new_user_builder.get_object('new_user_password')
		text1 = entry1.get_text()
	#end
	def new_user_submit(self, *args):
		uname = text
		passwd = text1
		if type(text) != None:
			with open(file, "w") as db:
				db.write(uname + ": " + passwd)
				db.write('\n')
				db.flush()
				db.close()
			#end
			print("Wrote to file")
		#end
		else:
			print("Cannot write info to file. No information given")
	#end
#end
#About
class about_menu:
	def about_quit(self, *args):
		Gtk.main_quit()
	#end
#end
#Help Menu
class help_handler:
	def help_menu_quit(self, *args):
		Gtk.main_quit()
	#end
	def help_menu_getting_started(self, *args):
		print("Work in progress")
	#end
	def help_menu_advanced_features(self, *args):
		print("Work in progess")
	#end
	def help_menu_about(self, *args):
		about_builder = Gtk.Builder()
		about_builder.add_from_file(path + "/glade-menus/" + "about.glade")
		about_builder.connect_signals(about_handler())
		about_obj = help_builder.get_object("about_main")
		about_obj.show_all()
		Gtk.main()
	#end
#end
#Main Menu
class handler:
	def menu_file_new_database(self, *args):
		if os.path.isfile(file):
			pass
		else:
			with open(file, "w+") as f:
				f.write("HEADER")
				f.write("\n")
				f.flush()
				f.close()
			#end
		#end
	#end
	def menu_file_new_user(self, *args):
		new_user_builder = Gtk.Builder()
		new_user_builder.add_from_file(path + "/glade-menus/" + "new_user.glade")
		new_user_builder.connect_signals(new_user_handler())
		new_user_obj = new_user_builder.get_object("user_main")
		new_user_obj.show_all()
		Gtk.main()
	#end
	def menu_file_new_user_default(self, *args):
		print("Feature not yet supported")
	#end
	def menu_file_edit_database(self, *args):
		print("Feature not yet supported")
	#end
	def menu_file_open_help(self, *args):
		help_builder = Gtk.Builder()
		help_builder.add_from_file(path + "/glade-menus/" + "help.glade")
		help_builder.connect_signals(help_handler())
		help_obj = help_builder.get_object("help_main")
		help_obj.show_all()
		Gtk.main()
	#end
	def menu_file_quit(self, *args):
		Gtk.main_quit()
#end
