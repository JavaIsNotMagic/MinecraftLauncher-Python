from CursesMenu import *
import socket,time

loginMenu = CursesMenu()

userID = CursesWidget("text", title="Username", onClose="listWidget")
userPWD = CursesWidget("text", title="Password", onClose=None)

loginMenu.addWidget(userID, id="root")
loginMenu.addWidget(userPWD, id="listWidget")

loginMenu.draw()

#TODO: Merge to secure socket

#Now send all the data to the server
host = socket.gethostname()
port = 10999

client_socket = socket.socket()
client_socket.connect((host, port))

message = f"{userID.value['text']}:{userPWD.value['text']}"

while True:
	try:	
		client_socket.send(str("new").encode())
		data = client_socket.recv(1024).decode()
		if data == "NEW USER: OK":
			print("Server is ready to accept new account")			
			client_socket.send(str("body").encode())
			data = None
		elif data == "DATA: OK":
			print("Creating new account!")			
			client_socket.send(message.encode())
			time.sleep(0.5)
			client_socket.send(str("end").encode())
			data = None
		else:
			print(f"Server sent {data}")
			data = None
	#end
	except BrokenPipeError:
		print("Server closed connection")
		break
#end
client_socket.close()
