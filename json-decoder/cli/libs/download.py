import re,sys,os
import urllib.request as ur
import urllib.error as ue
from urllib.parse import urlparse as up
#main
def getVersionUrl(file1, version, dp):
	#Don't even ask. It works. That's all that matters
	try:
		file = open(file1, "r")
		pass
	except:
		file = open(file1, "w+")
		file.write("")
		file.flush()
		file.close()
		file = open(file1, "r")
		pass
	#end
	string = version + ".json"
	flag = None
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
jarPath = str(os.getcwd() + "/downloads/mc/jars")	#Get the path to populate with files
try:
	os.mkdir(jarPath)	#Attempt to create the folder
	print("Created path for .jar files!")
except:
	pass	#Ignore if folder exists
#end
def downloadLibs(file2):	#Download libraries used by Minecraft
	file = open(file2, "r")	#Open the file specified in read only mode
	fileOutput = file.readlines()	#Get the content of the file line by line
	for line in fileOutput:	#For every line
		parseUrl = re.search(r'(?P<schema>http[s]?):\/\/(?P<siteName>(?P<subdomain>.{1,12})\.(?P<domain>.{1,10})\.(?P<tld>.{2,3}))\/(?P<path>.*(?P<fileName>\/.*\..*)$)', line.strip())	#Searches line using specified regex
		parseUrlDict = parseUrl.groupdict()	#Gets groups from regex result as a dictionary
		if parseUrlDict['subdomain'] == 'libraries':	#If the subdomain of the URL is a library:
			print(f"\nDownloading {parseUrlDict['fileName']}...")	#Debug
			currentPath = f"{jarPath}"	#Reset string
			for i in parseUrlDict['path'].split("/")[:-1]:	#Iterate through all parts of the path (except for the last which is the file)
				currentPath += "/" + i	#Add the folder name with a slash before it
				if not(os.path.isdir(currentPath)):	#If the folder doesn't exists:
					os.mkdir(currentPath)	#Attempt to make the folde
			savePath = f"{jarPath}/{parseUrlDict['path']}"	#Path of the file to save
			try:
				ur.urlretrieve(line, savePath)	#Download the file at the given URL and then save it to the specified path
			except:
				print(f"Error downloading {parseUrlDict['fileName']}.")
			print(f"Saved to {savePath}")	#Debug
		else:
			print(f"\nSkipping {parseUrlDict['fileName']}...")	#Debug
			continue	#Continue to next iteration if the URL does not have the 'libraries' subdomain

#	parseUrl regex documentation
#		(?P<schema>	- Creates a new named capture group
#			http	-Looks for the literal characters "http"
#			[s]?	-Zero or more of the literal "s"
#		)	-End named capture group
#		:	-Literal ":"
#		\/	-Literal "/"
#		\/	-Literal "/"
#		(?P<siteName>	-Named capture group
#			(?P<subdomain>	-Named capture group
#				.{1,12}	-1 to 12 of any character
#			)	-Close capture group
#			\.	-Literal "."
#			(?P<domain>	-Named capture group
#				.{1,10}	-1 to 10 of any character
#			)	-Close capture group
#			\.	-Literal "."
#			(?P<tld>	-Named capture group
#				.{2,3}	-2 to 3 characters
#			)	-Close capture group
#		)	-Close capture group
#		\/	-LIteral "/"
#		(?P<path>	-Named capture group
#			.*	-Any amount of characters
#			(?P<fileName>	-Named capture group
#				\/	-Literal "/"
#				.*	-Any amount of characters
#				\.	-Literal "."
#				.*	-Any amount of characters
#			)	-Named capture group
#			$	-Align capture group to end of line
#		)	-Close capture group
