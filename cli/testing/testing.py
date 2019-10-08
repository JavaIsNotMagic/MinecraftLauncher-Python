def getDownlodsTesting() :
	file_path = "C://Users/conno/Desktop/Development/Python/json-decoder/cli/pre-download/minecraft-versions.json"
	write_path = "C://Users/conno/Desktop/Development/Python/json-decoder/cli/pre-download/minecraft-download-url.txt"
	f = open(file_path, "r")
	urls = f.read()
	links = re.findall('"((http)s?://.*?)"', urls)
	for url in links:
		b = open(write_path, "w+")
		b.write(url[0])
		b.write('\n')
		b.flush()
		b.close()
	#end
#end