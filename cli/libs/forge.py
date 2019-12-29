import sys,os,re,json
from urllib.request import urlretrieve as ur
from urllib.error import *
#Custom imports
sys.path.append(str(os.getcwd()) + "/libs")
import utils

def fetchForgeSuperVersion():
	htmlFileLocation = ur("https://files.minecraftforge.net/maven/net/minecraftforge/forge/index_1.7.10.html")[0]	#Gets the contents at the URL, saves them to a tmpfile and gets the string to the path of that file
	fo = open(htmlFileLocation, "r")	#file object for HTML
	pageData = fo.read()	#Read HTML
	fo.close()	#Close HTML file
	#print(pageData) #debug
	pageSearch = re.finditer(r"index_((?:[0-9]+\.*){2,3})\.html", pageData)
	versions = []
	for match in pageSearch:
		#print(match.group(1)) #debug
		versions.append(match.group(1))
	return versions

#Return the Forge versions for the selected Vanilla version
def getForgeVersions(version):
	url = f"http://files.minecraftforge.net/maven/net/minecraftforge/forge/index_{version}.html"
	url_base = f"http://files.minecraftforge.net"
	if os.path.isdir(str(os.getcwd()) + "/downloads/mc/data"):
		store_decode = str(os.getcwd()) + "/downloads/mc/data/forge_versions_html" + version + ".txt"
		store = str(os.getcwd()) + "/downloads/mc/data/forge_versions_all" + version + ".txt"
		final = str(os.getcwd()) + "/downloads/mc/data/forge_versions" + version + ".txt"
	else:
		store_decode = str(os.getcwd()) + "/forge_versions_html" + version + ".txt"
		store = str(os.getcwd()) + "/forge_versions_all" + version + ".txt"
		final = str(os.getcwd()) + "/forge_versions" + version + ".txt"
	#download the file
	ur(url, store_decode)
	f = open(store_decode, "r")	#Opens the raw HTML file
	rawHTML = f.read()	#Reads content of the file
	f.close()	#Closes the file
	decodeRE = re.finditer(r"<a href=\"https://adfoc\.us/serve/sitelinks/\?id=\d+&url=(?P<URL>.+)\">\s+<i class=\".+\"></i>\s+Universal", rawHTML)	#Examine regex here: https://regex101.com/r/VnjD9o/2/
	with open(final, "w") as finalFile:	#Opens the final URL file
		for match in decodeRE:	#Goes through every match
			finalFile.write(match.groupdict()["URL"] + "\n")	#Write changes to URL file
			#print(match.groupdict()["URL"])	#Debug
		finalFile.close()	#Close URL file
	print(f"Got Forge versions for {version}!")
#end

try:
	getForgeVersions(sys.argv[1])
except IndexError:
	pass
#end

def parseVersions(version, returnVersion=None):
	#final = str(os.getcwd()) + "/forge_versions" + version + ".txt"
	if os.path.isdir(str(os.getcwd()) + "/downloads/mc/data"):
		versionsPath = str(os.getcwd()) + "/downloads/mc/data/forge_versions" + version + ".txt"
	else:
		versionsPath = str(os.getcwd()) + "/forge_versions" + version + ".txt"
	with open(versionsPath, "r") as fp:	#Opens the file with all the URLs for Forge versions
		versionsText = fp.read()	#Store as string
	if returnVersion != None:	#If a return version was specified
		for line in versionsText.split("\n"):	#Break the file up by line
			try:	#Catch errors
				if line.index(returnVersion):	#Try to find the version in the line, and if found then return. If it isn't found, str.index() raises a ValueError
					return line
			except ValueError:
				pass
		return False	#Return false if no URL was found for some reason...
	else:
		versions = []	#Store forge versions in list
		versionRe = re.finditer(r"(?P<version>\d+\.\d+\.\d+)-universal.jar$", versionsText, re.M)	#Find all versions in the forge_versions file (version-universal.jar$)
		for match in versionRe:	#For every match
			versions.append(match.groupdict()["version"])	#Add the match to the list of versions
		return versions	#Returns the list of versions
#end
def downloadForgeJar(url, version):
	try:
		os.mkdir(str(os.getcwd()) + "/downloads/mc/forge")
	except FileExistsError:
		pass
	#end
	print(f"Downloading Forge for version {version}")
	forge_save_path = str(os.getcwd()) + "/downloads/mc/forge/" + "forge" + version + ".jar"
	ur(url, forge_save_path)
#end
def downloadForgeLibs(version):
	ref_url = f"https://raw.githubusercontent.com/MinecraftForge/MinecraftForge/1.14.x/jsons/{version}-rel.json"
	download_url = "http://repo.maven.apache.org/maven2"
	super_path_start = str(os.getcwd()) + "/downloads/mc/jars"
	forge_jar = str(os.getcwd()) + "/downloads/mc/forge"
	data = []
	print(ref_url)
	forgeLocation = ur(ref_url)[0]
	with open(forgeLocation, 'r') as jsonFile:
		d = jsonFile.read()	#Raw data from the file
		jsonFile.close()
		jsonIter = re.finditer(r'^\ {6}\"name\": \"(?P<name>[^\"@]+)', d, re.M)	#Search file for regex
		for match in jsonIter:	#Iterate through all the matches
			mData = match.groupdict()["name"]
			#print(mData)
			nameSplit = list(re.search(r"^(?P<path>[^:]+):(?P<name>[^:]+):(?P<version>[^:]+)", mData).groups())
			nameSplit[0] = nameSplit[0].replace(r".", r"/")
			m_data = "/".join(nameSplit)
			#print(m_data) #debug
			lib_url = f"{download_url}/{nameSplit[0]}/{nameSplit[1]}/{nameSplit[2]}/{nameSplit[1]}-{nameSplit[2]}.jar"
			#Split the path into diectories
			dirs = nameSplit[0].split(os.sep)
			try:
				for x in dirs:
					if os.path.exists(super_path_start + "/" + x):
						#Path already exists.
						super_path = super_path_start + "/" + x
						pass
					else:
						os.mkdir(super_path_start + "/" + x)
						super_path = super_path_start + "/" + x
			except FileExistsError:
				pass
			#end
			print("Downloading: " + lib_url)
			try:
				lib_name = f"{nameSplit[1]}-{nameSplit[2]}.jar"
				ur(lib_url, super_path + "/" + lib_name)
				#add lib to classpath
				cp = str(os.getcwd()) + "/downloads/mc/data/classpath" + version + ".txt"
				with open(cp, "a") as cd:
					if sys.platform.startswith('nt'):
						sep = ';'
					else:
						sep = ":"
					#End
					cd.write(super_path + "/" + lib_name + sep)
			except HTTPError:
				print("Cannot download library. Skipping...")
				pass
		#end
		del data[:]
		print("Done!")
		cd.close()
		with open(cp, "a") as f:
			if sys.platform.startswith('nt'):
				sep = ';'
			else:
				sep = ":"
			#End
			
			#TODO: Find out why the following libs aren't already in the classpath
			f.write(f"{super_path_start}/net/minecraft/launchwrapper/1.12/launchwrapper-1.12.jar" + sep)
			f.write(f"{super_path_start}/org/apache/logging/log4j/log4j-api/2.0-beta9/log4j-api-2.0-beta9.jar" + sep)
			f.write(f"{super_path_start}/com/google/guava/guava/17.0/guava-17.0.jar" + sep)
			f.write(f"{super_path_start}/com/mojang/authlib/1.5.22/authlib-1.5.22.jar" + sep)
			f.write(f"{super_path_start}/com/google/code/gson/gson/2.2.4/gson-2.2.4.jar" + sep)
			#Should look like MCPY_INSTALL_PATH/cli/downloads/forge/forge<VERSION>.jar					
			print(f"Forge JAR: {forge_jar}/forge{version}.jar")					
			f.write(f"{forge_jar}/forge{version}.jar" + sep)
	#end
#end

