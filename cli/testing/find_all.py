import sys
def find_all(file, search):
	l1 = []
	a = open(file, "r")
	b = str(a.readlines())
	length = len(b)
	index = 0
	while index < length:
		i = b.find(search, index)
		if i == -1:
			r = int(str(l1).replace('[', '').replace(']', ''))
			q = length - r
			s = b[q]
			return l1, length, s
		l1.append(i)
		index = i + 1
	return l1, length
	a.close()
#end
print(find_all(sys.argv[1], sys.argv[2]))