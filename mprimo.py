def eprimo(p):
    div = 0
    
    for divisor in range(1, p):
        if p % divisor == 0:
            div += 1
            
        if div > 1:
          break
        
    if div > 1:
        return False
    
    else:
        return True

def maior_primo(m):
    primo = m
    i = 0
    while i <= m:
        if eprimo(i):
            primo = i
        i = i + 1
        
    return primo
