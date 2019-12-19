from os import walk,getcwd,remove

data = str(getcwd()) + "/downloads/mc/data"
data_launcher = str(getcwd()) + "/downloads/mc"
files = []
files1=[]

def clean():
	for(dirpath, dirnames,filenames) in walk(data):
		files.extend(filenames)
	#end

	for(dirpath, dirnames,filenames) in walk(data_launcher):
        	files1.extend(filenames)
	#end

	for x in files:
		#print(f"Removing file {data + '/' + x}") 
		try:
			remove(data + "/" + x)
		except FileNotFoundError:
			pass
	#end
	for a in files1:
		#print(f"Removing file {data_launcher + '/' + a}")
		try:
			remove(data_launcher + "/" + a)
		except FileNotFoundError:
			pass
#end
