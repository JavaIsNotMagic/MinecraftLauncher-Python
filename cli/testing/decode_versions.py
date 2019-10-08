import sys,re
#Lists
release_list = []
snapshot_list = []
beta_list = []
alpha_list = []
#File stuff
fd = open(sys.argv[1], "r")	#File Descriptor object from the command line
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
print("Releases:"   + str(release_list))
print("Snapshots: " + str(snapshot_list))
print("Beta: "      + str(beta_list))
print("Alpha: "     + str(alpha_list))