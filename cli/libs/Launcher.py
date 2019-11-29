import subprocess,os,platform,sys
def Launch(uname, version, game_directory, assets_root, atoken, client, classpath):
	#Test to see if java is installed
	testArgs = ["java", "-version"]
	try:
		subprocess.run(testArgs)
	except:
		print("Please install Java on your system to use mcpy.")
		sys.exit(1)
	#end
	launchArgs = ["java"] #Create the launcher arguments array
	#Natives are system dependent
	if platform.system() == "Linux":
		libpath = str(os.getcwd()) + "/downloads/mc/natives/linux"
	elif platform.system() == 'Windows':
		libpath = str(os.getcwd()) + "/downloads/mc/natives/windows"
	elif platform.system == 'macosx' or 'Darwin':
		libpath = str(os.getcwd()) + "/downloads/mc/natives/osx"
	else:
		print("Your system is not supported by mcpy.")
		sys.exit(1)
	#end
	cp = classpath + client
	empty = "{}"
	args = f"-Djava.library.path={libpath} -classpath {cp} net.minecraft.client.main.Main --username {uname} --version {version} --gameDir {game_directory} --assetsDir {assets_root} --assetIndex {version} --uuid {atoken} --accessToken {atoken} --userProperties {empty} --userType legacy" #Create a string to get all the arguments for the command to be executed
	launchArgs.extend(args.split(" "))	#Gets the arguments, splits it by spaces, adds the contents of that array to the existing array (https://stackoverflow.com/questions/252703/what-is-the-difference-between-pythons-list-methods-append-and-extend)
	#print(f"Command to run: {launchArgs}")	#Debug for command to run
	#Now run Minecraft given the information
	subprocess.run(launchArgs)
#end
