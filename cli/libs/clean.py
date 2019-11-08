"""
os: Operating System module, helper for file I/O operations (File exists check, etc)
"""
from os import walk,getcwd
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
		#print("Removing: " + data + "/" + i) #debug
		os.remove(data + "/" + i)
	#End
	for a in f:
		#print("Removing: " + downloads + "/" + a) #debug
		os.remove(downloads + "/" + a)
#end
