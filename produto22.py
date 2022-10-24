tamanho = int(input("Digite o tamanho da sequência de números:"))

produto = 1
i = 0 
valor = 1 
while i < tamanho:
	valor = int(input("Digite um valor a ser mutiplicado:"))
	produto = produto * valor
	i = i + 1

print ("O produto dos valores digitados é:", produto)