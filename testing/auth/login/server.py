import socket

#Data
data_file = open("user_data.txt", "w+")
data_file.write("HEADER\n")
#Server

host = socket.gethostname()
port = 10999

server_socket = socket.socket()
server_socket.bind((host, port))

#configure

server_socket.listen(4) #Up to four connections
conn,addr = server_socket.accept()

print(f"Client connected: {str(addr)}")

while True:
	data = conn.recv(1024).decode()
	if not data:
		break
	else:
		print(f"User sent: {str(data)}")
		if data == "new":
			message = "NEW USER: OK"
			conn.send(message.encode())
			data = None
		elif data == "body":
			data_file.write(f"{data}\n")
			conn.send(str("DATA: OK").encode())
			data = None
		elif data == "end":
			break
			data = None
		else:
			print(f"Client sent {data}")
			data = None
		#end
	#end
#end
conn.close()
data_file.close()
