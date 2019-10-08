import pip
packages_to_install=[gi]
if not packages_to_install == '[]':
	for i in packages_to_install:
		if hasattr(pip, 'main'):
			pip.main(['install', i])
		else:
			pip._internal.main(['install', i])
		#end
	#end
else:
	exit(0)
#end