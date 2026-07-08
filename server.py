import socket
import threading

# Set up the server on your own computer
host = '127.0.0.1'   # localhost
port = 12345         # any free port number

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

print("Server running..waiting for someone to connect.")

# Wait for one person to join
client, address = server.accept()
print("Connected to", address)

# Keep listening for their messages in the background
def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            print("\nFriend:", message)
        except:
            break

threading.Thread(target=receive).start()

# Keep sending your messages
while True:
    message = input("You: ")
    client.send(message.encode())