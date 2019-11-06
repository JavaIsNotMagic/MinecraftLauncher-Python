"""
os: Operating System module, helper for file I/O operations (File exists check, etc)
"""
import os
write_path = str(os.getcwd()) + "/downloads/urls.txt"
download_path_mc = str(os.getcwd()) + "/downloads/mc/data/download_urls.txt"
def clean():
	#Final stage
	print("Stage Five: Cleanup.")
	try:
		os.remove(write_path)
		if os.path.isfile(write_path):
			print("Could not remove version data")
		else:
			pass
		os.remove(download_path_mc)
		if os.path.isfile(download_path_mc):
			print("Could not remove minecraft data")
		else:
			pass
		print('Done!')
		#end
	except FileNotFoundError:
		pass
	#end
#end
resourcePath = str(os.getcwd()) + "/downloads/mc/assets/objects/"
def assets():
	for i in os.walk(resourcePath):
			if i[0] == resourcePath:
				pass
			else:
				if os.path.isfile(i[0]):
					os.remove(i[0])
				else:
					pass
				#end
			#end
		#end
	#end
#end
