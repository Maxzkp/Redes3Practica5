host = input()
ip = input()
varbind = []
while 1:
	try:
		varbind.append(input())
	except EOFError:
		print("Fin de la lectura")
		break

print(f'Demotrap Reconocida\n{host}\n{ip}\n{varbind}')