"""
re: Regex module, for URL parsing. see docs/regex/parseUrl.help for more info
os: Operating System module, helper for file I/O operations (File exists check, etc)
"""
import re, os
def decode_urls(dp, wp):
	f = open(dp, "r")
	urls = f.read()
	links = re.findall('"((http)s?://.*?)"', urls)
	try:
		os.mkdir(f'{os.getcwd()}/downloads/mc/data')
	except FileExistsError:
		pass
	#Probably caused by a glitch in the Matrix or we are testing new code. Ignore this.	
	except FileNotFoundError:
		pass
	b = open(wp, "w+")
	for url in links:
		b.write(f"{url[0]}\n")
		b.flush()
	#end
	b.close()
	print("Done!")
#end
def getLineIndex(fname, line2):
    with open(fname) as f:
        lines = [l.strip() for l in f.readlines()]
        for idx, line in enumerate(lines):
            if line2 in line:
                return idx
        return -1
#end
import re
def selectionHelper(file):
	#Lists
	release_list = []
	snapshot_list = []
	beta_list = []
	alpha_list = []
	#File stuff
	fd = open(file, "r")	#File Descriptor object from the command line
	fo = fd.read()	#File Output as a string of text read from the file specified
	fd.close()	#Close the file
	rePattern = re.compile(r'(?P<releaseJSON>{\"id\": \"(?P<id>(?:\w|\.|-| )*)\", \"type\": \"(?P<type>\w*)\", \"url\": \"(?P<url>https?://\w*\.\w*\.\w*(?:/(?:\w|\.|-)*)*\.\w*)\", \"time\": \"(?P<time>\d{4}-\d{1,2}-\d{2}T\d{2}:\d{2}:\d{2}\+\d{2}:\d{2})\", \"releaseTime\": \"(?P<releaseTime>\d{4}-\d{1,2}-\d{2}T\d{2}:\d{2}:\d{2}\+\d{2}:\d{2})\"})')	#Regex to parse URL's
	for i in re.finditer(rePattern, fo):	#For every found case in the JSON file:
		#print(f"\nData:\n\tRelease: {i['id']}\n\tType of release: {i['type']}\n\t")	#Show data for each release (as an example)
		if i['type'] == 'old_beta':
			beta_list.append(i['id'])
		elif i['type'] == 'old_alpha':
			alpha_list.append(i['id'])
		elif i['type'] == 'release':
			release_list.append(i['id'])
		elif i['type'] == 'snapshot':
			snapshot_list.append(i['id'])
		#end
	#end
	return release_list, snapshot_list, beta_list, alpha_list
#end
import json,uuid
def get_token(user):
	path = str(os.getcwd())
	atoken = str(uuid.uuid1()).strip('UUID')
	with open(path + "/minecraft/usernamecache.json", "w+") as f:
		f.write("{")
		f.write("\n")
		f.write('"' + f"{atoken}: {user}" + '"')
		f.write("}")
		f.write("\n")
		f.flush()
		f.close()
	#end
#end
	#end
	print("Got user authentication token")
	return atoken
#end
