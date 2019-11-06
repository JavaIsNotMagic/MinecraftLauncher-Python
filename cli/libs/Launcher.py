import os,json
args_file = str(os.getcwd()) + "/downloads/version_decoded.txt"
def Launch():
    my_dict = json.load(args_file)
    for i in my_dict['mainClass'].keys():
        print(my_dict['mainClass'][i])
    #end
#End
