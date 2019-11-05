import gi,os,sys
#Other Imports
path = os.getcwd()
file = path + "/data/" + "database.db"
#GUI
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
#Libraries
lib_path = str(os.getcwd()) + "/libs/glade"
sys.path.append(lib_path)
from globals import handler

#Main
builder = Gtk.Builder()
builder.add_from_file(path + "/glade-menus/" + "menu.glade")
builder.connect_signals(handler())

window = builder.get_object("window_menu")
window.connect("destroy", Gtk.main_quit)
window.show_all()

Gtk.main()