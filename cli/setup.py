import time, subprocess, os, sys
def PackageInstall(error):
	lib = str(error)[15:].replace('\'', '')
	print('>>>',str(error))
	print('>>> Download will start after five seconds')
	time.sleep(5)
	packages_to_install=open(str(os.getcwd() + "/requirements.txt")).readlines()
	for line in packages_to_install:
		lib = line
		subprocess.call("pip install " + lib)
#end
try:
    import pygame
except ImportError as error:
        PackageInstall(error)
	pass
#end