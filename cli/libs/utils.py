import re
def decode_urls(dp, wp):
	f = open(dp, "r")
	urls = f.read()
	links = re.findall('"((http)s?://.*?)"', urls)
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