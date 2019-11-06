"""
os: Operating System module, helper for file I/O operations (File exists check, etc)
"""
import os
downloads = str(os.getcwd()) + "/downloads/"
def clean():
	#Final stage
	print("Stage Five: Cleanup.")
	for i in os.path.walk(downloads):
		#Don't delete the downloads folder
		if i[0] == downloads:
			pass
		else:
			os.remove(i[0])
		#end
	#end
#end
