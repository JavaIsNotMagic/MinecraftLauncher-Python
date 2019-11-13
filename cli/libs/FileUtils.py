from sys import platform
from os import getcwd,walk
from zipfile import ZipFile
#Functions
def read_file(f):
  with open(f) as fp:
    return fp.read()
  #End
#end
def unpack_natives(version):
	classpath = str(getcwd()) + "/downloads/mc/data/classpath" + version + ".txt"
	with open(classpath, "r") as f:
		for line in f:
			if "natives-windows" in line:
				print("Windows Native: " + line, sep=":")
			elif "natives-linux" in line:
				print("Linux Native: " + line, sep=":")
			else:
				print("Mac Native: " + line, sep=":")
			#End
		#End
	#End
#end
