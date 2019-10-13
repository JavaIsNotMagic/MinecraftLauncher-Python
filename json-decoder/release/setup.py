import time, subprocess, os, sys
def PackageInstall(error):
	lib = str(error)[15:].replace('\'', '')
	print('>>>',str(error))
	print('>>> Download will start after five seconds')
	time.sleep(5)
	packages_to_install=open(str(os.getcwd() + "/requirements.txt")).readlines()
	for line in packages_to_install:
		lib = line
		os.system("pip3 install " + lib)
#end
try:
	import pygame
	import nacl.pwhash
except ImportError as error:
	PackageInstall(error)
	pass
#end
