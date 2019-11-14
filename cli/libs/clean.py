"""
os: Operating System module, helper for file I/O operations (File exists check, etc)
"""
from os import walk,getcwd,remove
downloads = str(getcwd()) + "/downloads/"
data = str(getcwd()) + "/downloads/mc/data"
def clean():
	#Final stage
	f = []
	g = []
	for(dirpath, dirnames, filenames) in walk(data):
		g.extend(filenames)
		break
	#end
	for(dirpath, dirnames, filenames) in walk(downloads):
		f.extend(filenames)
		break
	#end
	for i in g:
		print("Stage Seven: Removing " + data + "/" + i) #debug
		remove(data + "/" + i)
	#End
	for a in f:
		print("Stage Eight: Removing " + downloads + "/" + a) #debug
		remove(downloads + "/" + a)
#end
