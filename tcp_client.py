import socket

TCP_SERVER_ADDR = '127.0.0.1'
TCP_PORT = 3188
TCP_RX_BUF_SIZE_MAX = 128
TCP_CMD_TERM = 'Exit'
LOG_PREFIX = '[TCP Client] '

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect((TCP_SERVER_ADDR, TCP_PORT))

clientSocket.send(bytearray(TCP_CMD_TERM, 'utf-8'))

rxBuf = bytearray(TCP_RX_BUF_SIZE_MAX)
msgLen = clientSocket.recv_into(rxBuf, TCP_RX_BUF_SIZE_MAX)

print(LOG_PREFIX + 'Received response from Server:')
print(LOG_PREFIX + '    Message length: ' + str(msgLen))
print(LOG_PREFIX + '    Contents: ' + rxBuf.decode('utf-8'))