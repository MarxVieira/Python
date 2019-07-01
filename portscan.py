import socket
import sys

if len(sys.argv) == 1:
	print 'Executando scan no IP 192.168.15.1'
	for port in range(1,6200):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		if s.connect_ex(('192.168.15.1',port)) == 0:
			print 'Porta',port,'Aberta'
			s.close()
		if s.connect_ex(('192.168.15.1',port)) != 0:
			print 'Porta',port,'Fechada'
			s.close()

if len(sys.argv) == 2:
	ip = sys.argv[1]
	print 'Executando scan no IP',ip,'.'
	for porta in range(1,6200):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		if s.connect_ex((ip, porta)) == 0:
			print 'Porta',porta,'Aberta'
			s.close()
		if s.connect_ex((ip, porta)) != 0:
			print 'Porta',porta,'Fechada'
			s.close()