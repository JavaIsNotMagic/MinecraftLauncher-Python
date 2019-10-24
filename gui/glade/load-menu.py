import gi,os
#GUI
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
#Other Imports
path = os.getcwd()
file = path + "/data/" + "database.db"
text = None
text1 = None
#Main
class new_user_handler:
	def new_user_close(self, *args):
		Gtk.main_quit()
	#end
	def new_user_uname(self, *args):
		text = Gtk.Entry.get_text()
	#end
	def new_user_password(self, *args):
		text1 = Gtk.Entry.get_text()
	#end
	def new_user_submit(self, *args):
		uname = new_user_uname()
		passwd = new_user_password()
		with open(file, "w") as db:
			db.write(uname + ": " + passwd)
			db.write('\n')
			db.flush()
			db.close()
		#end
	#end
#end


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
		help_obj = help_builder.get_object("help_main")
		help_obj.show_all()
		Gtk.main()
	#end
	def menu_file_quit(self, *args):
		Gtk.main_quit()
#end
builder = Gtk.Builder()
builder.add_from_file(path + "/glade-menus/" + "menu.glade")
builder.connect_signals(handler())

window = builder.get_object("window_menu")
window.show_all()

Gtk.main()