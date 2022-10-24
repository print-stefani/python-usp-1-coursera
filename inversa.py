n = int(input('Digite um número: '))
lista = []
while n > 0:
    lista.append(n)
    x = int(input('Digite um número: '))
    n = x

lista_inversa = []
for numero in range(len(lista), 0, -1):
    lista_inversa.append(lista[numero - 1])

for i in lista_inversa:
    print(i)
