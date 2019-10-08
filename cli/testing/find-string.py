import re
import sys

file = open(sys.argv[2], "r")

for line in file:
	if re.search(sys.argv[1], line):
		print(line,)