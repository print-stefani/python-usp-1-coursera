



decrescente = True
anterior = int (input("digite o primeiro número de uma sequência decrescente:"))

valor = 1 

while valor != 0 and decrescente:
	valor = int (input("digite o próximo número decrescente:"))
	if valor > anterior:
		decrescente = False
	anterior = valor
if decrescente:
	print (	"Sequência correta! :)")
else:
	print ("Sequência incorreta, tente de novo :(")