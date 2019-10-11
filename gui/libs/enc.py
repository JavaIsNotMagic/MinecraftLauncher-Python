#NaCl
import nacl.secret
import nacl.utils
import nacl.pwhash
import os, base64
def getfile():
	file = str(os.getcwd() + "/data/unec/users.txt")
	a = open(file, "r")
	b = a.readlines()
	for line in b:
		if "Password: " in line:
			passwd = line.split(":")[2]
		#end
	#end
	return str(passwd)
#end

def encrypt():
	fpath = str(os.getcwd() + "/data/unec/nacl/salt.salt")
	users = str(os.getcwd() + "/data/unec/users.txt")
	users_file = str(os.getcwd() + "/data/1/users.txt")

	key_size = nacl.secret.SecretBox.KEY_SIZE
	salt_size = nacl.pwhash.argon2i.SALTBYTES
	salt = nacl.utils.random(salt_size)
	password = getfile()

	kdf = nacl.pwhash.argon2i.kdf
	key = kdf(key_size, password, salt)
	secret_msg = open(users.readlines())
	box = nacl.secret.SecretBox(key)
	enc = box.encrypt(secret_msg)
	text = base64.b64encode(enc).decode("ascii")
	with open(users_file, 'w+') as f:
		f.write(text)
		f.write('\n')
		f.flush()
		f.close()
	#end
#end