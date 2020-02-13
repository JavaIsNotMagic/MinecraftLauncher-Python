import ssl,socket,os

hostname = '127.0.0.1'
path=str(os.getcwd()) 

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations(f"{path}/cert.d/testing.pem")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
	#Connect to the server	
	sock.connect((hostname, 8443))
	with context.wrap_socket(sock, server_hostname=hostname) as ssock:
		print(ssock.version())
		ssock.send(str("Hello!").encode())
		data = ssock.recv(1024)
		print(f"Server sent: {data}")
#end
