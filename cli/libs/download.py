import re,sys,os
import urllib.request as ur
import urllib.error as ue
from urllib.parse import urlparse as up
#main
def getVersionUrl(file1, version, dp):
	file = open(file1, "r+")
	string = version + ".json"
	for line in file:
		if string in line:
			#print(line) #Debug
			flag = True
			break
		else:
			#print("Not found.") #Debug
			flag = False
			pass
		#end
	if flag:
		try:
			ur.urlretrieve(line, dp)
			print("Done!")
		except ue.URLError:
			print("Version " + version + " not found.")
			sys.exit(1)
		#end
	else:
		pass
	#end
#end
#paths
paths = {'jars': str(os.getcwd() + "/downloads/mc/jars"),	#Get the path for plain jar files
'windows': str(os.getcwd() + "/downloads/mc/jars/natives/windows"),	#Get the path for windows files
'osx': str(os.getcwd() + "/downloads/mc/jars/natives/osx"),	#Get the path for osx files
'linux': str(os.getcwd() + "/downloads/mc/jars/natives/linux") #Get the path for linux files
}

def downloadLibs(file2):	#Download libraries used by Minecraft
	file = open(file2, "r")	#Open the file specified in read only mode
	fileOutput = file.readlines()	#Get the content of the file line by line
	for line in fileOutput:	#For every line
		#print(line)	#Debug
		parseUrl = re.search(r'(?P<schema>http[s]?):\/\/(?P<siteName>(?P<subdomain>.{1,10})\.(?P<domain>.{1,10})\.(?P<tld>.{2,3}))\/(?P<path>.*(?P<fileName>\/.*\..*)$)', line)	#Searches line using specified regex
		"""
		(?P<schema>	- Creates a new named capture group
			http	-Looks for the literal characters "http"
			[s]?	-Zero or more of the literal "s"
		)	-End named capture group
		:	-Literal ":"
		\/	-Literal "/"
		\/	-Literal "/"
		(?P<siteName>	-Named capture group
			(?P<subdomain>	-Named capture group
				.{1,10}	-1 to 10 of any character
			)	-Close capture group
			\.	-Literal "."
			(?P<domain>	-Named capture group
				.{1,10}	-1 to 10 of any character
			)	-Close capture group
			\.	-Literal "."
			(?P<tld>	-Named capture group
				.{2,3}	-2 to 3 characters
			)	-Close capture group
		)	-Close capture group
		\/	-LIteral "/"
		(?P<path>	-Named capture group
			.*	-Any amount of characters
			(?P<fileName>	-Named capture group
				\/	-Literal "/"
				.*	-Any amount of characters
				\.	-Literal "."
				.*	-Any amount of characters
			)	-Named capture group
			$	-Align capture group to end of line
		)	-Close capture group
		"""
		try:
			parseUrlDict = parseUrl.groupdict()	#Gets groups from regex result as a dictionary
			#print(parseUrlDict) #Debug
			pass
			#print('\n\n', parseUrlDict, parseUrl)	#Debug
			#print('\n\n', parseUrlDict['path'], parseUrlDict['fileName'])	#Debug
		except:
			#print("Error parsing URL.")
			pass
		save_path = None	#Python didn't like my method for defining variables
		try:	#Try to execute the following code:
			url3 = up(line)	#Parse the URL contained in the line
			name3 = os.path.basename(url3.path)	#Gets the final part (filename) of the url path
			if 'natives-windows' in line:	#If 'natives-windows' is found in the line
				save_path = f"{paths['windows']}/{str(name3).strip()}"	#Joins the folder name to download to with the file's name
			elif 'natives-osx' in line:	#If 'natives-osx is found in the line
				save_path = f"{paths['osx']}/{str(name3).strip()}"	#Joins the folder name to download to with the file's name
			elif 'natives-linux' in line:	#If 'natives-linux is found in the line
				save_path = f"{paths['linux']}/{str(name3).strip()}"	#Joins the folder name to download to with the file's name
			elif '.jar' in line:	#If '.jar' is found in the line
				save_path = f"{paths['jars']}/{str(name3).strip()}"	#Joins the folder name to download to with the file's name
			else:	#If the test doesn't work
				print(f"\nNo valid type found in\n\t{line.strip()}\nSkipping...")	#Debug
				continue	#Skip the rest of the execution for this iteration
			#Gets file at the URL at the line and saves it to the specified location
			print(f"\nDownloading...\n\t{line.strip()}")	#Debug
			
			if parseUrlDict['subdomain'] == 'libraries':
				currentPath = ""
				for i in parseUrlDict['path'].split("/")[:-1]:
					currentPath += "/" + i
					#print(currentPath) #Debug
					try:
						#print("Making dir: " + paths['jars'] + currentPath) #Debug
						os.mkdir(paths['jars'] + currentPath)
					except:
						pass
				#end
				fpath = paths['jars'] + "/" + parseUrlDict['path']
				ur.urlretrieve(line, fpath)
			else:
				continue
			#end
			#print(f"Downloaded to\n\t{fpath}")	#Debug			
		except ue.URLError as a:	#If there's an error with the above code:
			print(f"{os.path.basename(up(line).path)} not found.\tReason: {str(a)}")	#Debug