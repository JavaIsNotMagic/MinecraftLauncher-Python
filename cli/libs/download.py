import re,sys,os,traceback
import urllib.request as ur
import urllib.error as ue
from urllib.parse import urlparse as up
libs_path = str(os.getcwd())+ "/libs"
sys.path.append(libs_path)
import utils
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
	cp = str(os.getcwd()) + "/downloads/mc/data/classpath.txt"
	try:
		with open(cp, "w+") as cd:
			cd.write('\n')
			cd.flush()
			cd.close()
	except:
		print("Cannot create classpath file")
		sys.exit(1)
	#end
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
			try:#Download the file at the given URL and then save it to the specified path
				ur.urlretrieve(line, savePath)
				#Now save that path to the classpath.
				with open(cp, "a") as r:
					if sys.platform.startswith('nt'):
						sep = ';'
					else:
						sep = ":"
					#End
					r.write(savePath + sep)
					r.flush()
					r.close()
					#print("Wrote path: " + savePath + " to classpath") # DEBUG
					#print(f"Saved to {savePath}")	#Debug
			except:
				print(f"Error downloading {parseUrlDict['fileName']}.")
				exc_type, exc_value, exc_traceback = sys.exc_info()
				trace_back = traceback.extract_tb(exc_traceback)
		        # Format stacktrace
				stack_trace = list()
				for trace in trace_back:
					stack_trace.append("File : %s , Line : %d, Func.Name : %s, Message : %s" % (trace[0], trace[1], trace[2], trace[3]))
					print("Exception type : %s " % exc_type.__name__)
					print("Exception message : %s" %exc_value)
					print("Stack trace : %s" %stack_trace)
		else:
			print(f"\nSkipping {parseUrlDict['fileName']}...")	#Debug
			continue	#Continue to next iteration if the URL does not have the 'libraries' subdomain
"""
	parseUrl regex documentation
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
#End
resourcePath = str(os.getcwd()) + "/downloads/mc/assets"
jsonPath = str(os.getcwd()) + "/downloads/mc/data/data.json"
jsonPath1 = str(os.getcwd()) + "/downloads/mc/data/resources.json"
try:
	os.mkdir(resourcePath)	#Attempt to create the folder
	print("Created path for MC Assets!")
except:
	pass	#Ignore if folder exists
#end
def downloadResources(version, dp):
	utils.decode_urls(dp, jsonPath1)
	with open(jsonPath1) as f:
		for line in f.readlines():
			if version in line:
				ur.urlretrieve(line, jsonPath)
		f.close()
	#end
	with open(jsonPath, 'r') as p:
		for line in p:
			parseUrl = re.search(r'(?P<schema>http[s]?):\/\/(?P<siteName>(?P<subdomain>.{1,12})\.(?P<domain>.{1,10})\.(?P<tld>.{2,3}))\/(?P<path>.*(?P<fileName>\/.*\..*)$)', line.strip())	#Searches line using specified regex
			parseUrlDict = parseUrl.groupdict()	#Gets groups from regex result as a dictionary
			#If the subdomain of the URL is a library:
			print(f"\nDownloading {parseUrlDict['fileName']}...")	#Debug
			currentPath = f"{resourcePath}"	#Reset string
			for i in parseUrlDict['path'].split("/")[:-1]:	#Iterate through all parts of the path (except for the last which is the file)
				currentPath += "/" + i	#Add the folder name with a slash before it
				if not(os.path.isdir(currentPath)):	#If the folder doesn't exists:
					os.mkdir(currentPath)	#Attempt to make the folde
					savePath = f"{resourcePath}/{parseUrlDict['path']}"
			#End
		#End
	#End
#End
