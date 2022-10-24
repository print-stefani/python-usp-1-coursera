
lar = int(input("Digite a largura: "))
alt = int(input("Digite a altura: "))

linha = 0
coluna = 0

while linha < alt:
    while coluna < lar:
        print ("#", end= "")
        coluna += 1
    print ()
    linha += 1
    coluna = 0
