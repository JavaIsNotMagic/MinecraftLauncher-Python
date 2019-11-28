import subprocess,os,platform
def Launch(uname, version, game_directory, assets_root, atoken, client, classpath):
	launchArgs = ["java"] #Create the launcher arguments array
	#Natives are system dependent
	if platform.system() == "Linux":
		libpath = str(os.getcwd()) + "/downloads/mc/natives/linux"
	elif platform.system() == 'Windows':
		libpath = str(os.getcwd()) + "/downloads/mc/natives/windows"
	else:
		libpath = str(os.getcwd()) + "/downloads/mc/natives/osx"
	#end
	cp = classpath + client
	empty = "{}"
	args = f"-Djava.library.path={libpath} -classpath {cp} net.minecraft.client.main.Main --username {uname} --version {version} --gameDir {game_directory} --assetsDir {assets_root} --assetIndex {version} --uuid {atoken} --accessToken {atoken} --userProperties {empty} --userType legacy" #Create a string to get all the arguments for the command to be executed
	launchArgs.extend(args.split(" "))	#Gets the arguments, splits it by spaces, adds the contents of that array to the existing array (https://stackoverflow.com/questions/252703/what-is-the-difference-between-pythons-list-methods-append-and-extend)
	#print(f"Command to run: {launchArgs}")	#Debug for command to run
	#Now run Minecraft given the information
	subprocess.run(launchArgs, shell=False, check=True)
#end
