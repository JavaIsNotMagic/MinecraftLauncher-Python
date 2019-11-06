import os
args_file = str(os.getcwd()) + "/downloads/version_decoded.txt"
def Launch():
    with open(args_file) as f:
        for line in f:
            if "minecraftArguments" in line:
                print(line)
            #End
        #end
    #End
#End
