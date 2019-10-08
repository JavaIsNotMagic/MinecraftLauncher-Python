import json,sys
file = open(sys.argv[1], "r")
for line in file.readlines():
	if 'path' in line:
		print(line)
	#end
#end