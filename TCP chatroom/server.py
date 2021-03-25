import threading
import sockets

host ='127.0.0.1'  #localhost
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((host,port))
server.listen()

clients= []
nicknames =[]

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while true:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index= client.index(client)
            clients.remove(client)
            client.clode()
            nickname=nickname[index]
            broadcast (f'{nickname} left the chat !'.encode('ascii'))

            nicknames.remove(nickname)
            break
      
def receive():
    while True:
        client, address = server.accept()
        print(f"connected with {str (address)}")

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        cliets.append(client)

        print(f"nickname of the client is{nickname}")
        broadcast (f'{nickname} joined the chat'.encode('ascii'))
        client.send('connected to the server'.encode('ascii'))

        thread = threading.Thread(target=handle, arg=(client,))
        thread.start()

receive()