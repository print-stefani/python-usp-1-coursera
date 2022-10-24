n = int(input("Digite um número inteiro: "))
cond = True

while cond:
    x_1 = n % 10
    x = n // 10
    x_2 = x % 10
    if n <= 10:
        print('não')
        cond = False
    elif n > 10 and x_1 == x_2:
        print('sim')
        cond = False
    else:
        n = n//10