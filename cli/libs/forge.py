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
	#for line in f.readlines():
	#	if "(Direct Download)" in line:
	#		if "universal" in line:
	#			#print(line) #debug
	#			with open(store, "w") as r:
	#				r.write(re.sub('\s+',' ', line))
	#				r.write('\n')
	#				r.flush()
	#				r.close()
	#			#end
	#		#end
	#	else:
	#		pass
	#	#end
	##end
	#lines = []
	#with open(store, "r") as t:
	#	for line in t.readlines():
	#		if "<a href=" in line:
	#			#print(line.replace(">", "").replace("<", "").replace("br", "").replace("a href=", "").replace(r'"', "").replace(r"(Direct Download)", "").replace(r"/a", "")) #debug
	#			lines.append(line.replace(">","").replace("<","").replace("br","").replace("a href=","").replace(r'"',"").replace(r"(Direct Download)","").replace(r"/a",""))
	#	#end
	#	t.flush()
	#	t.close
	##end
	#with open(final, "w") as y:
	#	for x in lines:
	#		url_full = url_base + x
	#		y.write(re.sub('\s+','', url_full))
	#		y.write('\n')
	#		y.flush()
	#	#end
	#	y.close()
	#end
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

def downloadForgeLibs(version):
	ref_url = f"https://raw.githubusercontent.com/MinecraftForge/MinecraftForge/1.14.x/jsons/{version}-rel.json"
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
			print(m_data)
			#m_data = "/".join(mData.split('.')).replace(r":", "/")	#Match DATA
			#data.append(m_data)
		#end
		del data[:]
	#end
#end

"""
net/minecraft/launchwrapper/1.9

path.replace(., /)
[path, name, version].join(/)

path net.minecraft -> net/minecraft
path/name/version


(path net.minecraft):(name launchwrapper):(version 1.9)
org.ow2.asm:asm-all:4.1
org.scala-lang:scala-library:2.10.2
org.scala-lang:scala-compiler:2.10.2
java3d:vecmath:1.3.1
net.sf.trove4j:trove4j:3.0.3
com.ibm.icu:icu4j-core-mojang:51.2
net.sf.jopt-simple:jopt-simple:4.5
lzma:lzma:0.0.1
com.paulscode:codecjorbis:20101023
com.paulscode:codecwav:20101023
com.paulscode:libraryjavasound:20101123
com.paulscode:librarylwjglopenal:20100824
com.paulscode:soundsystem:20120107
io.netty:netty-all:4.0.10.Final
com.google.guava:guava:15.0
org.apache.commons:commons-lang3:3.1
commons-io:commons-io:2.4
net.java.jinput:jinput:2.0.5
net.java.jutils:jutils:1.0.0
com.google.code.gson:gson:2.2.4
com.mojang:authlib:1.3
org.apache.logging.log4j:log4j-api:2.0-beta9
org.apache.logging.log4j:log4j-core:2.0-beta9
org.lwjgl.lwjgl:lwjgl:2.9.0
org.lwjgl.lwjgl:lwjgl_util:2.9.0
org.lwjgl.lwjgl:lwjgl-platform:2.9.0
org.lwjgl.lwjgl:lwjgl:2.9.1-nightly-20131017
org.lwjgl.lwjgl:lwjgl_util:2.9.1-nightly-20131017
org.lwjgl.lwjgl:lwjgl-platform:2.9.1-nightly-20131017
net.java.jinput:jinput-platform:2.0.5
"""
