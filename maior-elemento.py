def maior_elemento(numeros):
    maiorNumero = 0

    for numeroCorrente in numeros:
        if numeroCorrente > maiorNumero or maiorNumero == 0:
            maiorNumero = numeroCorrente

    return maiorNumero

print(maior_elemento([-90, -27, -12]))
