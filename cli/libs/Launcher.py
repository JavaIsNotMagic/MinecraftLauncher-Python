import subprocess,sys,os
def Launch(uname, version, game_directory, assets_root, atoken, client, classpath):
    launcher = os.getcwd() + "/libs/launcher.sh"
    file1 = os.getcwd() + "/libs/launch-args.txt"
    #There is a trailing colon in the cp. Don't add one
    cp = classpath + client
    empty = "{}"
    args = f"-classpath  {cp}  net.minecraft.client.main.Main --username  {uname} --version {version} --gameDir  {game_directory} --assetsDir  {assets_root}  --assetIndex  {version} +  --uuid  {atoken} --accessToken  {atoken} --userProperties {empty} --userType legacy"
    with open(file1, "w+") as f:
        f.write(args)
        f.flush()
        f.close()
        print(str(f.read()))
        sys.exit(12)
    try:
        subprocess.run(["/bin/bash", launcher], shell=False, check=True)
    except subprocess.CalledProcessError:
        print("Could not launch Minecraft")
        sys.exit(12)
#end
