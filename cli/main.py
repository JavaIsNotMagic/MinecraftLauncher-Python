#!/usr/bin/env python3
"""
re: Regex module, for URL parsing. see docs/regex/parseUrl.help for more info
sys: System module, various helper tasks.
os: Operating System module, helper for file I/O operations (File exists check, etc)
urllib.request: Used to download files from the internet
urllib.error: Error classes for urllib.request. Needed for urllib.*
selection: Helper module to select version to launch
download: Various helper functions to download Minecraft's assets and libraries
clean: Cleanup after launch. Removes temporary files
utils: various helper functions
"""

import re, os, sys
import urllib.request
import urllib.error as ue
#Custom libs
libs_path = str(os.getcwd())+ "/libs"
sys.path.append(libs_path)
import selection, download, clean, utils
from Launcher import Launch
#CLI Check
try:
	if sys.argv[1] == 'clean':
		clean.clean()
		sys.exit(20)
	else:
		pass
	if sys.argv[1] == 'clean-assets':
		clean.assets()
		sys.exit(20)
except IndexError:
	pass
#end

write_path = str(os.getcwd()) + "/downloads/urls.txt"
download_path = str(os.getcwd()) + "/downloads/vm.json"
version_decoded = str(os.getcwd() + "/downloads/version_decoded.txt")
download_urls = str(os.getcwd() + "/downloads/mc/data/download_urls.txt")
url = "https://launchermeta.mojang.com/mc/game/version_manifest.json"
path = str(os.getcwd())

try:
	os.mkdir(str(os.getcwd()) + "/downloads")
	os.mkdir(str(os.getcwd()) + "/downloads/mc")
	os.mkdir(str(os.getcwd()) + "/downloads/mc/data")
except FileExistsError:
	pass
#end

print("Decoding Minecraft assets at path " + path)
print("Stage one: Download Version Manifest")
try:
	if os.path.isfile(download_path):
		print("Done")
		pass
	else:
		urllib.request.urlretrieve(url, download_path)
		print("Done")
		print("Stage two: Seperate URLs from Version Manifest")
		if os.path.isfile(write_path):
			print("Done")
			pass
		else:
			utils.decode_urls(download_path, write_path)
		#end
	#end
except ue.URLError:
	print("Cannot continue. Version Manifest not found")
	sys.exit(1)
#end


print("Stage three: Select Version to Download")
print("Version Types")
print("Release (1)" + ' ' + "Snapshot (2)")
print("Beta (3)" + ' ' + "Alpha (4)")
try:
	ans = int(input(">:"))
	pass
except KeyboardInterrupt:
	sys.exit(10)
#end

#Release
if ans == 1:
	version = selection.pr()
	print("Stage Four: Download Minecraft Assets")
	print("Downloading Version: " + version)
	download.getVersionUrl(write_path, version, version_decoded)
	utils.decode_urls(version_decoded, download_urls)
	download.downloadLibs(download_urls)
	download.downloadResources(version, download_path)
	print("Launching Minecraft " + version)
	Launch()
	clean.clean()
	clean.assets()
#end

#Snapshot
if ans == 2:
	version = selection.psn()
	print("Downloading Version: " + version)
	download.getVersionUrl(write_path, version, version_decoded)
	utils.decode_urls(version_decoded, download_urls)
	download.downloadLibs(download_urls)
	download.downloadResources(version, download_path)
	Launch()
	clean.clean()
	clean.assets()
#end

#Beta
if ans == 3:
	version = selection.pb()
	print("Downloading Version: " + version)
	download.getVersionUrl(write_path, version, version_decoded)
	utils.decode_urls(version_decoded, download_urls)
	download.downloadLibs(download_urls)
	download.downloadResources(version, download_path)
	Launch()
	clean.clean()
	clean.assets()
#Alpha
if ans == 4:
	version = selection.pa()
	print("Downloading Version: " + version)
	download.getVersionUrl(write_path, version, version_decoded)
	utils.decode_urls(version_decoded, download_urls)
	download.downloadLibs(download_urls)
	download.downloadResources(version, download_path)
	Launch()
	clean.clean()
	clean.assets()
#end
