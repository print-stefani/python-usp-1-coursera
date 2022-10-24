seucartao = int(input("Digite os números do seu cartão de crédito: "))

cartaolido = 1
encontreicartao = False

while cartaolido != 0 and not encontreicartao:
	cartaolido = int(input("Digite os números do proximo cartão: "))
	if cartaolido == seucartao:
		encontreicartao = True

if encontreicartao:
	print ("EBA, seu cartão foi encontrado!!")
else:
	print ("Ops.. seu cartão não esta na lista :( ")