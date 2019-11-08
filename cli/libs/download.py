"""
re: Regex module, for URL parsing. see docs/regex/parseUrl.help for more info
sys: System module, various helper tasks.
os: Operating System module, helper for file I/O operations (File exists check, etc)
traceback: Complex error report and capture module
urllib.request: Used to download files from the internet
urllib.error: Error classes for urllib.request. Needed for urllib.*
urlparse: General URL classes.
json: JSON handler module: needed to decode Minecraft's .json files
utils: various helper functions
"""

import re,sys,os,traceback
import urllib.request as ur
import urllib.error as ue
from urllib.parse import urlparse as up
import json
#from pprint import pprint as pp

#Custom Libs
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
			with open(dp, "r") as f:
				string = f.readlines()
				for line in string:
					if version in line:
						pass
					else:
						print("Version: " + version + " not downloaded")
						sys.exit(21)
			#print("Done!")
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
def downloadLibs(file2,version):	#Download libraries used by Minecraft
	cp = str(os.getcwd()) + "/downloads/mc/data/classpath" + version + ".txt"
	client_path = str(os.getcwd()) + "/downloads/mc/versions/client" + version + ".jar"
	try:
		with open(cp, "w+") as cd:
			if sys.platform.startswith('nt'):
				sep = ';'
			else:
				sep = ":"
			#End
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
		file_name = parseUrlDict['fileName'].strip("/")
		if parseUrlDict['subdomain'] == 'libraries':	#If the subdomain of the URL is a library:
			print(f"\nDownloading {file_name}...")	#Debug
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
					print("Wrote path: " + savePath + " to classpath") # DEBUG
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
			#We need client.jar. This is Minecraft.
			if file_name == "client.jar":
				ur.urlretrieve(line, client_path)
			else:
				pass
			print(f"\nSkipping {file_name}...")	#Debug
			continue	#Continue to next iteration if the URL does not have the 'libraries' subdomain
#End
resourcePath = str(os.getcwd()) + "/downloads/mc/assets/objects/"
jsonPath = str(os.getcwd()) + "/downloads/mc/data/data.json"
jsonPath1 = str(os.getcwd()) + "/downloads/mc/data/resources.json"
dp1 = str(os.getcwd()) + "/downloads/mc/data/full.json"
assets_list = str(os.getcwd()) + "/downloads/mc/data/assets.json"
resource_base = "http://resources.download.minecraft.net/"
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
				#print(line)
				ur.urlretrieve(line, jsonPath)
				utils.decode_urls(jsonPath, dp1)
				#print("Done.")
	f.close()
	with open(dp1) as f:
		for line in f.readlines():
			if ".json" in line:
				#print(line)
				ur.urlretrieve(line, assets_list)
				#Make a copy for the Index list
				index_list = str(os.getcwd()) + "/downloads/mc/assets/indexes/" + version + ".json"
				ur.urlretrieve(line, index_list)
				#print("done.")
	f.close()
	hash_two = []
	hash_full = []
	with open(assets_list) as f:
		my_dict = json.load(f)
		for i in my_dict['objects'].keys():
			hash_full_obj = my_dict['objects'][i]['hash']
			hash_first_two = my_dict['objects'][i]['hash'][:2]
			hash_two.append(hash_first_two)
			hash_full.append(hash_full_obj)
			#print("Full hash: " + hash_full) #Debug
			#print("First two: " + hash_first_two) #Debug
		#end
		for x in hash_two:
			currentPath = resourcePath + x
			if not(os.path.isdir(currentPath)):
				os.mkdir(currentPath)
			#end
		#end
		#Now donload the files to the folders
		n = 0
		catch_all = len(hash_full) - 1
		while n <= catch_all:
			try:
				url = resource_base + hash_two[n] + "/" + hash_full[n]
			except IndexError:
				pass
			#end
			file_path = resourcePath + hash_two[n] + "/" + hash_full[n]
			if os.path.exists(file_path):
				n += 1
			else:
				print("Downloading file " + str(n) + " of " + str(catch_all))
				ur.urlretrieve(url, file_path)
				n+=1
			#print(file_path) ## DEBUG:
		#end
	#end
#end
