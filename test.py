import socket 
import json

def createJSON(text):
    obj = {}
    obj['type'] = 'speechToText'
    data = {}
    data['text'] = text
    obj['data'] = json.dumps(data)
    return json.dumps(obj)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def sendMessage(text):
	try:
		socketaddress = ('10.131.222.198', 1336)
		data = createJSON(text)
		sock.connect(socketaddress)
		sock.sendall(data.encode())
	finally:
		sock.close()

sendMessage('hi')
