import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8003))
server_socket.listen(1)


while True:
   
    data = conn.recv(1024).decode()
    if not data:
        break
    print('Received data:', data)

  
    data=[x for x in data]
    if data [0]=="A":
        data.remove("A")
        data.sort()
        data=" ".join(data)
        data=data.replace(" ","")
       
        
    elif data[0]=="C":
        data.remove("C")
        data=" ".join(data)
        data=data.replace(" ","")
        data = data.upper()
    elif data[0]=="D":
        data.remove("D")
        data=sorted(data,reverse=True)
        data=" ".join(data)
        data=data.replace(" ","")
    

    
        
    conn.sendall(data.encode())

conn.close()
