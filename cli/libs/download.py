import re,sys,os
import urllib.request as ur
import urllib.error as ue
from urllib.parse import urlparse as up
#main
def getVersionUrl(file1, version, dp):
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
paths = {'jars': str(os.getcwd() + "/downloads/mc/jars")}	#Get the path for plain jar files
try:
	os.mkdir(paths['jars'])
except:
	pass
#end
def downloadLibs(file2):	#Download libraries used by Minecraft
	file = open(file2, "r")	#Open the file specified in read only mode
	fileOutput = file.readlines()	#Get the content of the file line by line
	print(fileOutput)	#Debug
	for line in fileOutput:	#For every line
		final = line.strip()
		parseUrl = re.search(r'(?P<schema>http[s]?):\/\/(?P<siteName>(?P<subdomain>.{1,12})\.(?P<domain>.{1,10})\.(?P<tld>.{2,3}))\/(?P<path>.*(?P<fileName>\/.*\..*)$)', final)	#Searches line using specified regex
		print(parseUrl)
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
				.{1,12}	-1 to 12 of any character
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
		#Try to execute the following code:
		try:
			#Gets file at the URL at the line and saves it to the specified location
			parseUrlDict = parseUrl.groupdict()	#Gets groups from regex result as a dictionary
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