#teste funcao fatorial

def fatorial (n):
    fat = 1
    while (n > 1):
        fat = fat * n
        n = n - 1
    return fat

def num_binominal (n,k):
    return fatorial (n) // (fatorial(k) * fatorial(n-k))

def test_fat():
    if fatorial (1) == 1:
        print ("funciona para 1")
    else:
        print ("NÃO funciona para 1")
        
    if fatorial (2) == 2:
        print ("funciona para 2")
    else:
        print ("NÃO funciona para 2")

    if fatorial (0) == 1:
        print ("funciona para 0")
    else:
        print ("NÃO funciona para 0")
        
    if fatorial (5) == 120:
        print ("funciona para 5")
    else:
        print ("NÃO funciona para 5")



    
