"""
os: Operating System module, helper for file I/O operations (File exists check, etc)
"""
import os
downloads = str(os.getcwd()) + "/downloads/"
def clean():
	#Final stage
	print("Stage Five: Cleanup.")
	for i in os.walk(downloads):
		try:
			os.remove(i[0])
		except IsADirectoryError:
			pass
		#end
	#end
#end
