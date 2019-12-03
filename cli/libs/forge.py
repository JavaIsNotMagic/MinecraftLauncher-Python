import sys,os,re
from urllib.request import urlretrieve as ur
#Custom imports
sys.path.append(str(os.getcwd()) + "/libs")
import utils

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
	f = open(store_decode, "r")
	for line in f.readlines():
		if "(Direct Download)" in line:
			if "universal" in line:
				#print(line) #debug
				with open(store, "a+") as r:
					r.write(re.sub('\s+',' ', line))
					r.write('\n')
					r.flush()
					r.close()

				#end
			#end
		else:
			pass
		#end
	#end
	lines = []
	with open(store, "r") as t:
		for line in t.readlines():
			if "<a href=" in line:
				#print(line.replace(">", "").replace("<", "").replace("br", "").replace("a href=", "").replace(r'"', "").replace(r"(Direct Download)", "").replace(r"/a", "")) #debug
				lines.append(line.replace(">","").replace("<","").replace("br","").replace("a href=","").replace(r'"',"").replace(r"(Direct Download)","").replace(r"/a",""))
		#end
		t.flush()
		t.close
	#end
	with open(final, "a+") as y:
		for x in lines:
			url_full = url_base + x
			y.write(re.sub('\s+','', url_full))
			y.write('\n')
			y.flush()
		#end
		y.close()
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
