# From https://docs.python.org/2/library/asyncore.html
# Modified by: Chris Pavlicek

import asyncore, socket

class SocketClient(asyncore.dispatcher):
	def __init__(self, host, port):
		asyncore.dispatcher.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.connect( (host, port) )
		self.buffer = "HELLO"

	def handle_connect(self):
		pass

	def handle_close(self):
		self.close()

	def handle_read(self):
		print self.recv(8192)

	def writable(self):
		return (len(self.buffer) > 0)

	def handle_write(self):
		sent = self.send(self.buffer)
		self.buffer = self.buffer[sent:]

client = SocketClient('localhost', 8080)
client2 = SocketClient('localhost', 8080)
client3 = SocketClient('localhost', 8080)
client4 = SocketClient('localhost', 8080)
asyncore.loop()
