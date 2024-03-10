import socket

HEADER  = 64 #size of actual message
FORMAT = 'utf-8'
PORT = 5050
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT) 
DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client.connect(ADDR)

# def send(message):
#     message = message.encode(FORMAT)

#     #message_length = len(message)
#     #send_length = str(message_length).encode(FORMAT)   
#     #send_length += b' ' * (HEADER - len(send_length))

#     #client.send(send_length)
#     client.send(message)

client.send("Hello".encode(FORMAT))
print(client.recv(1024).decode(FORMAT))
print(client.recv(1024).decode(FORMAT))
#print(client.recv(1024).decode(FORMAT))

while(True):
   

    question = input()
    
    client.send(question.encode(FORMAT))
    
    r = client.recv(1024).decode(FORMAT)
    print(r)

    if(r == "Invalid question" or r == "stop"):
        break
    else:
        continue
    



#client.send(DISCONNECT_MESSAGE)