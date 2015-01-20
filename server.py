# From https://docs.python.org/2/library/asyncore.html
# Modified by: Chris Pavlicek

import asyncore
import socket

class EchoHandler(asyncore.dispatcher_with_send):

	def handle_read(self):
		data = self.recv(8192)
		if data:
			if data.find(chr(27)) >= 0:
				self.close()
			data = data.strip()
			self.send("{} {}\n".format(data,"Chris"))

class SocketServer(asyncore.dispatcher):
	def __init__(self, host, port):
		asyncore.dispatcher.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.set_reuse_addr()
		self.bind((host, port))
		self.listen(5)
	
	def handle_accept(self):
		pair = self.accept()
		if pair is not None:
			sock, addr = pair
			print 'Incoming connection from %s' % repr(addr)
			handler = EchoHandler(sock)

server = SocketServer('localhost', 8080)
asyncore.loop()
