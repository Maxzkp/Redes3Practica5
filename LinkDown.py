from MailControl import sendMail
import re
from datetime import datetime

host = input()
ip = input()
varbind = []
while 1:
	try:
		varbind.append(input())
	except EOFError:
		print("Fin de la lectura")
		break

info = [line.split() for line in varbind]
oids = ''
interface = ''
for i in info:
	if re.search(r'eth.*', i[1]):
		interface = i[1]
	else:
		oids += f'{i[0]}\t=>\t{i[1]}\n'

strspan = re.search(r'\[[^\[\]]*\]', ip).span()

hostip = ip[strspan[0]+1:strspan[1]-1]

day = datetime.today().strftime('%Y-%m-%d')

hour = datetime.today().strftime('%H:%M')

subject = f'Desconexion de la interfaz {interface} del host {host}'

content = f'El {day} a las {hour} horas ha sido desconectada la interfaz {interface} del host {host} con ip {hostip}\n\nVariables recibidas\n{oids}'



print(f'Sent!')
sendMail(subject, content, 'saulcabrera.zk@gmail.com')
#sendMail(subject, content, 'tanibet.escom@gmail.com')