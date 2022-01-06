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
from CursesMenu import *	#Self promotion because why not: https://github.com/scoutchorton/CursesMenu
import urllib.request
import urllib.error as ue
import uuid
#Custom libs
libs_path = str(os.getcwd())+ "/libs"
sys.path.append(libs_path)
import selection, download, clean, utils
from Launcher import Launch,LaunchForge
from FileUtils import read_file
from forge import getForgeVersions, parseVersions, fetchForgeSuperVersion, downloadForgeLibs, downloadForgeJar
from check_libs import check
#CLI Check
try:
	if sys.argv[1] == 'clean':
		clean.clean()
		sys.exit(20)
	else:
		pass
except IndexError:
	pass
#end

#CursesMenu integration
	#CursesMenu initialization
mainMenu = CursesMenu()
	#CursesMenu widgets initialization
username = CursesWidget("text", title="In-Game Username:")
versionType = CursesWidget("list", title="Version Type:")
versionList = CursesWidget("list", title="Version:")
	#CursesMenu adding widgets
mainMenu.addWidget(username, margin=2, id="username")
mainMenu.addWidget(versionType, margin=2, id="versionType")
mainMenu.addWidget(versionList, margin=2, id="version")



write_path = str(os.getcwd()) + "/downloads/urls.txt"
download_path = str(os.getcwd()) + "/downloads/vm.json"
version_decoded = str(os.getcwd() + "/downloads/version_decoded.txt")
download_urls = str(os.getcwd() + "/downloads/mc/data/download_urls.txt")
url = "https://launchermeta.mojang.com/mc/game/version_manifest.json"
gameDir = str(os.getcwd()) + "/minecraft/game"
path = str(os.getcwd())
try:
	os.mkdir(str(os.getcwd()) + "/minecraft")	
	os.mkdir(str(os.getcwd()) + "/downloads")
	os.mkdir(str(os.getcwd()) + "/downloads/mc")
	os.mkdir(str(os.getcwd()) + "/downloads/mc/data")
	os.mkdir(str(os.getcwd()) + "/downloads/mc/jars")
	os.mkdir(str(os.getcwd()) + "/downloads/mc/versions")
	os.mkdir(str(os.getcwd()) + "/downloads/mc/assets")
	os.mkdir(str(os.getcwd()) + "/downloads/mc/assets/objects")
	os.mkdir(str(os.getcwd()) + "/downloads/mc/assets/indexes")
except FileExistsError:
	pass
#end
mainMenu.draw("username")	#Initate the CursesMenu widget
#uname = input("Berfore we begin, please enter your desired in-game username: ")
uname = username.value["text"]
print("Thank you for using PyMC " + uname + "!")
print("Decoding Minecraft assets at path " + path)
print("Stage one: Download Version Manifest")
try:
	if os.path.isfile(download_path):
		os.remove(download_path)
		urllib.request.urlretrieve(url, download_path)
		#print("Done")
		print("Stage two: Seperate URLs from Version Manifest")
		if os.path.isfile(write_path):
			os.remove(write_path)
			utils.decode_urls(download_path, write_path)
		else:
			utils.decode_urls(download_path, write_path)
		#end
	else:
		urllib.request.urlretrieve(url, download_path)
		#print("Done")
		print("Stage two: Seperate URLs from Version Manifest")
		if os.path.isfile(write_path):
			os.remove(write_path)
			utils.decode_urls(download_path, write_path)
		else:
			utils.decode_urls(download_path, write_path)
		#end
	#end
except ue.URLError:
	print("Cannot continue. Version Manifest not found")
	sys.exit(1)
#end


#print("Stage three: Select Version to Download")
#print("Version Types")
#print("Release (1)" + ' ' + "Snapshot (2)")
#print("Beta (3)" + ' ' + "Alpha (4)")
versionType.data = ["Release", "Snapshot", "Beta", "Alpha", "Forge"]
mainMenu.draw("versionType")
try:
	#ans = int(input(">:"))
	ans = versionType.value["index"] + 1
	pass
except KeyboardInterrupt:
	sys.exit(10)
#end

#Release
if ans == 1:
	version = selection.pr()
	versionList.data = version	#Set array of versions to the data to be displayed by versionList
	mainMenu.draw("version")
	version = versionList.value["text"]
	print("Stage Four: Download Minecraft Assets")
	print("Downloading Version: " + version)
	download.getVersionUrl(write_path, version, version_decoded)
	utils.decode_urls(version_decoded, download_urls)
	download.downloadLibs(download_urls, version)
	rpath = download.downloadResources(version, download_path)
	print("Stage Five: Unpacking Natives")
	download.extractNatives(rpath)
	print("Done!")
	print("Stage Six: Launching Minecraft " + version)
	check(version)
	assetsDir = str(os.getcwd()) + "/downloads/mc/assets"
	atoken = utils.get_token(uname)
	client = str(os.getcwd()) + "/downloads/mc/versions/client" + version + ".jar"
	cp = path + "/downloads/mc/data/classpath" + version + ".txt"
	classpath = read_file(cp)
	Launch(uname, version, gameDir, assetsDir, atoken, client, classpath)
	clean.clean()

#end

#Snapshot
if ans == 2:
	version = selection.psn()
	versionList.data = version	#Set array of versions to the data to be displayed by versionList
	mainMenu.draw("version")
	version = versionList.value["text"]
	print("Stage Four: Download Minecraft Assets")
	print("Downloading Version: " + version)
	download.getVersionUrl(write_path, version, version_decoded)
	utils.decode_urls(version_decoded, download_urls)
	download.downloadLibs(download_urls, version)
	rpath = download.downloadResources(version, download_path)
	print("Stage Five: Unpacking Natives")
	download.extractNatives(rpath)
	print("Done!")
	print("Stage Six: Launching Minecraft " + version)
	check(version)
	assetsDir = str(os.getcwd()) + "/downloads/mc/assets"
	atoken = utils.get_token(uname)
	client = str(os.getcwd()) + "/downloads/mc/versions/client" + version + ".jar"
	cp = path + "/downloads/mc/data/classpath" + version + ".txt"
	classpath = read_file(cp)
	Launch(uname, version, gameDir, assetsDir, atoken, client, classpath)
	clean.clean()

#end

#Beta
if ans == 3:
	version = selection.pb()
	versionList.data = version	#Set array of versions to the data to be displayed by versionList
	mainMenu.draw("version")
	version = versionList.value["text"]
	print("Stage Four: Download Minecraft Assets")
	print("Downloading Version: " + version)
	download.getVersionUrl(write_path, version, version_decoded)
	utils.decode_urls(version_decoded, download_urls)
	download.downloadLibs(download_urls, version)
	rpath = download.downloadResources(version, download_path)
	print("Stage Five: Unpacking Natives")
	download.extractNatives(rpath)
	print("Done!")
	print("Stage Six: Launching Minecraft " + version)
	check(version)
	assetsDir = str(os.getcwd()) + "/downloads/mc/assets"
	atoken = utils.get_token(uname)
	client = str(os.getcwd()) + "/downloads/mc/versions/client" + version + ".jar"
	cp = path + "/downloads/mc/data/classpath" + version + ".txt"
	classpath = read_file(cp)
	Launch(uname, version, gameDir, assetsDir, atoken, client, classpath)
	clean.clean()

#Alpha
if ans == 4:
	version = selection.pa()
	versionList.data = version	#Set array of versions to the data to be displayed by versionList
	mainMenu.draw("version")
	version = versionList.value["text"]
	print("Stage Four: Download Minecraft Assets")
	print("Downloading Version: " + version)
	download.getVersionUrl(write_path, version, version_decoded)
	utils.decode_urls(version_decoded, download_urls)
	download.downloadLibs(download_urls, version)
	rpath = download.downloadResources(version, download_path)
	print("Stage Five: Unpacking Natives")
	download.extractNatives(rpath)
	print("Done!")
	print("Stage Six: Launching Minecraft " + version)
	assetsDir = str(os.getcwd()) + "/downloads/mc/assets"
	check(version)
	atoken = utils.get_token(uname)
	client = str(os.getcwd()) + "/downloads/mc/versions/client" + version + ".jar"
	cp = path + "/downloads/mc/data/classpath" + version + ".txt"
	classpath = read_file(cp)
	Launch(uname, version, gameDir, assetsDir, atoken, client, classpath)
	clean.clean()
#end

#FORGE
if ans == 5:
	vanillaVersions = selection.pr()
	versionList.data = fetchForgeSuperVersion()
	mainMenu.draw("version")
	selectedVanilla = versionList.value["text"]
	getForgeVersions(selectedVanilla)
	forgeVersions = parseVersions(selectedVanilla)
	versionList.title = "Forge Version:"
	versionList.data = forgeVersions
	mainMenu.draw("version")
	forgeVersion = parseVersions(selectedVanilla, versionList.value["text"])
	#print(forgeVersion) #debug
	#use versionList.value["text"] for the version.
	downloadForgeJar(forgeVersion, selectedVanilla)
	downloadForgeLibs(selectedVanilla)
	assetsDir = str(os.getcwd()) + "/downloads/mc/assets"
	check(selectedVanilla)
	atoken = utils.get_token(uname)
	version = selectedVanilla
	client = str(os.getcwd()) + "/downloads/mc/forge/" + "forge" + version + ".jar"
	cp = path + "/downloads/mc/data/classpath" + version + ".txt"
	classpath = read_file(cp)
	LaunchForge(uname, version, gameDir, assetsDir, atoken, client, classpath)
	clean.clean()
#end
