import ssl,socket,os
path = str(os.getcwd())

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(f'{path}/cert.d/testing.pem', f'{path}/cert.d/testing.key')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    sock.bind(('127.0.0.1', 8443))
    sock.listen(5)
    print("Server ready to accept connections at 127.0.0.1:8443")
    with context.wrap_socket(sock, server_side=True) as ssock:        
        conn, addr = ssock.accept()
        ssock.send(str("Hello!").encode())
        data = conn.recv(1024)
        if not data:
             pass
        else:
            print(f"Client Sent: {data}")
#end
