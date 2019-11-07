"""
sys: System module, various helper tasks.
os: Operating System module, helper for file I/O operations (File exists check, etc)
"""
import os,sys
libs_path = str(os.getcwd())+ "/libs"
sys.path.append(libs_path)
import utils
download_path = str(os.getcwd()) + "/downloads/vm.json"
def pr():
	release = utils.selectionHelper(download_path)[0]
	for counter in range(len(release)):
			print(" Release " + str(counter) + '\t\t' + release[counter] + '\t\t', end='\t')
			if counter == range(len(release)):
				break
			else:
				pass
			#end
	#end
	counter = range(len(release))
	a = int(input("Enter Version Number: "))
	if a in counter:
		version = release[a]
		print("Version selected: " + version)
		return str(version)
	else:
		print("Please select a number between zero and " + len(release))
	#end
#end
def psn():
	snapshot = utils.selectionHelper(download_path)[1]

	for counter in range(len(snapshot)):
		print("Snapshot " + str(counter) + '\t' + '\t' + snapshot[counter] + '\t' + '\t', end='\t')
		if counter == range(len(snapshot)):
				break
		else:
			pass
			#end
	#end
	counter = range(len(snapshot))
	a = int(input("Enter Version Number: "))
	if a in counter:
		version = snapshot[a]
		print("Version selected: " + version)
		return str(version)
	else:
		print("Please select a number between zero and " + len(snapshot))
#end
def pb():
	beta = utils.selectionHelper(download_path)[2]
	for counter in range(len(beta)):
		print("Release " + str(counter) + '\t' + '\t' + beta[counter] + '\t' + '\t', end='\t')
		if counter == range(len(beta)):
			break
		else:
			pass
			#end
	#end
	counter = range(len(beta))
	a = int(input("Enter Version Number: "))
	if a in counter:
		version = beta[a]
		print("Version selected: " + version)
		return str(version)
	else:
		print("Please select a number between zero and " + len(beta))
#end
def pa():
	alpha = utils.selectionHelper(download_path)[3]
	for counter in range(len(alpha)):
		print("Release " + str(counter) + '\t' + '\t' + alpha[counter] + '\t' + '\t', end='\t')
		if counter == range(len(alpha)):
			break
		else:
			pass
		#end
	#end
	counter = range(len(alpha))
	a = int(input("Enter Version Number: "))
	if a in counter:
		version = alpha[a]
		print("Version selected: " + version)
		return str(version)
	else:
		print("Please select a number between zero and " + len(alpha))
#end
