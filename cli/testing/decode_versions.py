import sys,re
file = open(sys.argv[1], "r").readlines()
for line in file:
	a = re.compile(r'(?P<releaseJSON>{\"id\": \"(?P<id>(?:\w|\.|-| )*)\", \"type\": \"(?P<type>\w*)\", \"url\": \"(?P<url>https?://\w*\.\w*\.\w*(?:/(?:\w|\.|-)*)*\.\w*)\", \"time\": \"(?P<time>\d{4}-\d{1,2}-\d{2}T\d{2}:\d{2}:\d{2}\+\d{2}:\d{2})\", \"releaseTime\": \"(?P<releaseTime>\d{4}-\d{1,2}-\d{2}T\d{2}:\d{2}:\d{2}\+\d{2}:\d{2})\"})')
	match = re.search(a, line)
	print(match.groupdict()['id'] + match.groupdict()['type'])
#end
