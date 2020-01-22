import socket
from datetime import datetime

TCP_PORT = 3188
TCP_RX_BUF_SIZE_MAX = 128
TCP_CMD_TERM = 'Exit'
LOG_PREFIX = '[TCP Server] '

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind(('', TCP_PORT))

serverSocket.listen(5)

print(LOG_PREFIX + 'Listening at port: ' + str(TCP_PORT))

while True:
    client, clientAddr = serverSocket.accept()
    print(LOG_PREFIX + 'Connection has been established with: ' + str(clientAddr))
    
    rxBuf = bytearray(TCP_RX_BUF_SIZE_MAX)
    msgLen = client.recv_into(rxBuf, TCP_RX_BUF_SIZE_MAX)
    rxMsg = rxBuf.decode('utf-8')
    print(LOG_PREFIX + 'Message from client: ' + rxMsg)
    
    
    time = datetime.now().strftime("%H:%M:%S")
    txMsg = LOG_PREFIX + '[' + time + ']' + ' Thank for connecting'
    
    client.send(bytearray(txMsg, 'utf-8'))
    client.close()
    
    if -1 != str.find(rxMsg, TCP_CMD_TERM):
        break;
    
serverSocket.close()
