#NaCl
import nacl.secret
import nacl.utils
import nacl.pwhash
import os, base64, re
#GLOBALS
fpath = str(os.getcwd() + "/data/unec/nacl/salt.salt")
users = str(os.getcwd() + "/data/unec/users.txt")
users_file = str(os.getcwd() + "/data/1/users.txt")

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

def decrypt():
	password = getfile().encode('utf-8')
	with open(fpath, "r") as f:
		salt = re.sub(r'"', '', f.read().replace('b', '')).encode('utf-8')
		kdf = nacl.pwhash.argon2i.kdf
		key = kdf(nacl.secret.SecretBox.KEY_SIZE, password, salt)
		with open(users_file, "r") as g:
			content = g.read()
			enc = base64.b64decode(content)
			g.close()
		#end
		box = nacl.secret.SecretBox(key)
		msg = box.decrypt(enc)
		secret_msg = msg.decode('utf-8')
		return secret_msg
#end

#end
def encrypt():
	salt_size = nacl.pwhash.argon2i.SALTBYTES
	salt = nacl.utils.random(salt_size)
	with open(fpath, "w+") as h:
		h.write("Salt: " + salt)
		h.flush()
		h.close()
	#end
	password = getfile().encode('utf-8')

	kdf = nacl.pwhash.argon2i.kdf
	key = kdf(nacl.secret.SecretBox.KEY_SIZE, password, salt)
	msg = open(users, "r")
	secret_msg = str(msg.readlines()).encode('utf-8') 
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