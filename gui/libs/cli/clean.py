import os
write_path = str(os.getcwd()) + "/downloads/urls.txt"
download_path_mc = str(os.getcwd()) + "/downloads/mc/data/download_urls.txt"
download_path = str(os.getcwd()) + "/downloads/vm.json"
def clean():
	#Final stage
	print("Stage Five: Cleanup.")
	try:
		os.remove(write_path)
		if os.path.isfile(write_path):
			print("Could not remove version data")
		else: 
			pass
		os.remove(download_path)
		if os.path.isfile(download_path):
			print("Could not remove version info")
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
