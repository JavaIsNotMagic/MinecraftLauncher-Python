import subprocess
def Launch(uname, version, game_directory, assets_root, atoken, classpath, client):
    empty = "{}"
    args = f"java -jar {client} -cp {classpath} --username {uname} --version {version} --gameDir {game_directory} --assetsDir {assets_root} --assetIndex {version} --uuid {atoken} --accessToken {atoken} --userProperties {empty} --userType legacy"
    subprocess.run(["java", args], shell=False, check=True)
#end
