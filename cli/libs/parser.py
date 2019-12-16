import os
version = "1.7.10"
file = open(str(os.getcwd()) + f"/forge_versions{version}.txt")
for line in file.readlines():
	if "-1.7.10-" in line:
		line_new = line.replace(r"-1.7.10-", "-").replace("ls", "").replace(r"1710", "").replace(r"--", "-")
		print(os.path.basename(line_new))
	else:
		print(os.path.basename(line))
#end

