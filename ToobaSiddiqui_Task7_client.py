import socket
import threading

# Connect to the server
host = '127.0.0.1'
port = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

print("Connected to the chat!")

# Keep listening for messages in the background
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
