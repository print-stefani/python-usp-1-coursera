def eprimo (x):
    fator = 2
    if x == 2:
        return True
    while x % fator != 0 and fator <= x / 2:
        fator += 1
    if x % fator == 0:
        return False
    else:
        return True

n = int (input("Digite um numero inteiro: "))

while n > 0:
    if eprimo (n):
        print (n, "é primo")
    else:
        print (n, "não é primo")
    n = int (input("Dugite um numero inteiro: "))


def eprimo (x):
    fator = 2
    while x % fator != 0 and fator <= x / 2:
        fator += 1
    if x % fator == 0:
        return False
    else:
        return True
