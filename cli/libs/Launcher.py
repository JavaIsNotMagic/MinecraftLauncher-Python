import subprocess,sys,os
def Launch(uname, version, game_directory, assets_root, atoken, client, classpath):
    
    args = f"-classpath  {cp}  net.minecraft.client.main.Main --username  {uname} --version {version} --gameDir  {game_directory} --assetsDir  {assets_root}  --assetIndex  {version} +  --uuid  {atoken} --accessToken  {atoken} --userProperties {empty} --userType legacy"
