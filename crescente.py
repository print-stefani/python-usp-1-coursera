

crescente = True
posterior = int(input("Digite o primeiro número de uma sequência crescente (máx. até 100): "))

valor = 1

while valor != 100 and crescente:
	valor = int(input("Digite o proximo número crescente:"))
	if valor < posterior:
		crescente = False
	posterior = valor

if crescente: 
	print ("A sequência está em ordem crescente!")
else:
	print ("A sequência não em ordem crescente :(")


