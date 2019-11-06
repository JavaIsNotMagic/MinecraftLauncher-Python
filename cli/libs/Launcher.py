import subprocess,sys
def Launch(uname, version, game_directory, assets_root, atoken, client, classpath):
    empty = "{}"
    args = f"-classpath '{classpath}' -jar {client}  --username {uname} --version {version} --gameDir {game_directory} --assetsDir {assets_root} --assetIndex {version} --uuid {atoken} --accessToken {atoken} --userProperties {empty} --userType legacy"
    #print(args) #debug
    #sys.exit(12)
    try:
        subprocess.run(["java", args], shell=False, check=True)
    except subprocess.CalledProcessError:
        print("Could not launch Minecraft")
        sys.exit(12)
#end
