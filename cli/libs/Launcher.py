def Launch(uname, version, game_directory, assets_root, atoken, classpath, client):
    args = f"java -cp {classpath} -jar {client} mainClass net.minecraft.client.main.Main --username {uname} --version {version} --gameDir {game_directory} --assetsDir {assets_root} --assetIndex {version} --uuid {atoken} --accessToken {atoken} --userProperties --userType legacy"
    print(args)
#end
