n = int (input ("digite um numero inteiro maior que 1: "))

fator = 2
mult = 0

while n > 1:
    while n % fator == 0:
        mult += 1
        n = n / fator
    if mult > 0:
        print (" O fator %0.0f multiplicidade = %0.0f" % (fator, mult))
    fator += 1
    mult = 0
