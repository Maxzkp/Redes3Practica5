host = input()
ip = input()
varbind = []
while 1:
	try:
		varbind.append(input())
	except EOFError:
		print("Fin de la lectura")
		break

content = ''
for line in varbind:
	content += f'{line}\n'

print(f'\n\nCold Start\n\n{host}\n{ip}\n{content}')