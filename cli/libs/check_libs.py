from os import walk,getcwd
import sys

datapath = str(getcwd()) + "/downloads/mc/jars"
data = []

def check(version):
	classpath = open(str(getcwd()) + f"/downloads/mc/data/classpath{version}.txt")
	for(dirpath, dirnames, filenames) in walk(datapath):
		data.extend(filenames)
	#end
	length = len(classpath.read())
	n=0
	while n < length:	
		for i in data:
			if i in classpath.read():
				print(f"Library {i} found in classpath!")
				n+=1
		
			else:
				if "natives-windows" or("natives-macos") or("natives-osx")in line:
					n+=1
				else:			
					print(f"Library {i} not found. Cannot launch Minecraft")
					sys.exit(22)
			#end
		#end
	#end
	classpath.close()
#end
