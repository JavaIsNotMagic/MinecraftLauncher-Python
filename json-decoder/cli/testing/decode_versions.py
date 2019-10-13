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
<<<<<<< HEAD
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
=======
	print(f"\nData:\n\tRelease: {i['id']}\n\tType of release: {i['type']}\n\tURL for release data: {i['url']}\n\tTime?: {i['time']}\n\tRelease time: {i['releaseTime']}")	#Show data for each release (as an example)

"""
Version filter regex documentation:
	(?P<releaseJSON>	Start named capture group releaseJSON
		{\"id\": \"	Literal {"id": "
		(?P<id>	Start named capture group id
			(?:	State non-capturing group
				\w	Any word character
				|	or
				\.	Literal period
				|	or
				-	Literal dash
				|	or
				 	Literal space
			)*	End non-capturing group, repeated any amout of times
		)	End named capture group id
		\", \"type\": \"	Literal ", "type": "
		(?P<type>	Start named capture group type
			\w*	Any amount of word characters
		)	End named capture group type
		\", \"url\": \"	Literal ", "url": "
		(?P<url>	Start named capture group url
			http	Literal http
			s?	Zero or one s
			://	Literal ://
			\w*	Any amount of word characters
			\.	Literal period
			\w*	Any amount of word characters
			\.	Literal period
			\w*	Any amount of word characters
			(?:	Start non-capturing group
				/	Literal /
				(?:	Start non-capturing group
					\w	A single word character
					|	or
					\.	Literal period
					|	or
					-	Literal dash
				)*	End non-capturing group; zero or more of group
			)*	End non-capturing group; zero or more of group
			\.	Literal period
			\w*	Any amount of word characters
		)	End named capture group url
		\", \"time\": \"	Literal ", "time": "
		(?P<time>	Start named capture group time
			\d{4}	Four digits
			-	Literal dash
			\d{1,2}	One to two digits
			-	Literal dash
			\d{2}	Two digits
			T	Literal T
			\d{2}	Two digits
			:	Literal colon
			\d{2}	Two digits
			:	Literal colon
			\d{2}	Two digits
			\+	Literal plus
			\d{2}	Two digits
			:	Literal colon
			\d{2}	Two digits
		)	End named capture group time
		\", \"releaseTime\": \"	Literal ", "releaseTime": "
		(?P<releaseTime>	Start named capture group releaseTime
			\d{4}	Four digits
			-	Literal dash
			\d{1,2}	One to two digits
			-	Literal dash
			\d{2}	Two digits
			T	Literal T
			\d{2}	Two digits
			:	Literal colon
			\d{2}	Two digits
			:	Literal colon
			\d{2}	Two digits
			\+	Literal plus
			\d{2}	Two digits
			:	Literal colon
			\d{2}	Two digits
		)	End named capture group releaseTime
		\"}	Literal "}
	)	End named capture group releaseJSON
"""
>>>>>>> 7bcace790cd61559079b8a08a7958ac89f5fae82
