import urllib.request as ur
from PIL import Image
import pyotp,sys,base64,hashlib,hmac,os,time,struct


def verify(string):
	nstr = string	
	secret = 'AJXDWJX7ATUID35R'
    	# raise if nstr contains anything but numbers
	int(nstr)
	tm = int(time.time() / 30)
	secret = base64.b32decode(secret)
	# try 30 seconds behind and ahead as well
	for ix in [-1, 0, 1]:
		# convert timestamp to raw bytes
		b = struct.pack(">q", tm + ix)
		# generate HMAC-SHA1 from timestamp based on secret key
		hm = hmac.HMAC(secret, b, hashlib.sha1).digest()
		# extract 4 bytes from digest based on LSB
		offset = ord(hm[:-1]) & 0xFF
		truncatedHash = hm[offset:offset+4]
		# get the code from it
		code = struct.unpack(">L", truncatedHash)[0]
		code &= 0x7FFFFFFF;
		code %= 1000000;
		if ("%06d" % code) == nstr:
			return True
			print("AUTHENTICATED")
	print("Could not authenticate")	
	return False

def main():
	email = input("Enter email ")
	thing = email.split(r"@")
	code='AJXDWJX7ATUID35R'
	string = f"https://chart.googleapis.com/chart?chs=530x530&cht=qr&chl=otpauth%3A//totp/{thing[0]}%2540{thing[1]}%3Fsecret%3D{code}%26issuer%3DMinecraftLauncher%2520Python&choe=UTF-8"
	ur.urlretrieve(string, "chart.png")
	Image.open("chart.png").show()
	a = input("Got it? ")
	if a == "yes" or("Yes") or("Y") or("y"):
		code = input('enter code ')
		verify(code)
	else:
		print("Ill wait.")
		pass
	#end
#end
main()
