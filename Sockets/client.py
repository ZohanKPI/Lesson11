import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 12345

try:
    clientsocket.connect((host, port))
    while True:
        message = input("Enter your message: ")
        clientsocket.send(message.encode())

        response = clientsocket.recv(1024)
        print("Received response: %s" % response.decode())

        clientsocket.close()

except ConnectionRefusedError:
    print("Connection refused by the server")
except OSError as e:
    print(f"Socket error: {e}")