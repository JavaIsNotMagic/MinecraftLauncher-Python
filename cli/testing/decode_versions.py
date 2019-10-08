import sys,re
fd = open(sys.argv[1], "r")	#File Descriptor object from the command line
fo = fd.read()	#File Output as a string of text read from the file specified
fd.close()	#Close the file
rePattern = re.compile(r'(?P<releaseJSON>{\"id\": \"(?P<id>(?:\w|\.|-| )*)\", \"type\": \"(?P<type>\w*)\", \"url\": \"(?P<url>https?://\w*\.\w*\.\w*(?:/(?:\w|\.|-)*)*\.\w*)\", \"time\": \"(?P<time>\d{4}-\d{1,2}-\d{2}T\d{2}:\d{2}:\d{2}\+\d{2}:\d{2})\", \"releaseTime\": \"(?P<releaseTime>\d{4}-\d{1,2}-\d{2}T\d{2}:\d{2}:\d{2}\+\d{2}:\d{2})\"})')	#Regex to parse URL's
for i in re.finditer(rePattern, fo):	#For every found case in the JSON file:
	print(f"\nData:\n\tRelease: {i['id']}\n\tType of release: {i['type']}\n\tURL for release data: {i['url']}\n\tTime?: {i['time']}\n\tRelease time: {i['releaseTime']}")	#Show data for each release (as an example)
