import math

def delta (a,b,c):
        return b**2 - 4 * a * c

def main ():
        a_user = float (input ("Digite o valor de a: "))
        b_user = float (input ("Digite o valor de b: "))
        c_user = float (input ("Digite o valor de c: "))
        imprime_raizes (a_user,b_user,c_user)

def imprime_raizes (a,b,c):
        d = delta (a,b,c)
        
        if d < 0:
                print ("Esta equação não possui raizes reais")
        else:	
                raiz_1 = (-b + math.sqrt(d))/(2*a)
                raiz_2 = (-b - math.sqrt(d))/(2*a)

                if d == 0:
	
                        print ("A unica raiz é:",'{:.2f}'.format(raiz_1))
                else:
		
                        print ("A primeira raiz é:",'{:.2f}'.format(raiz_1))
                        print ("A segunda raiz é:", '{:.2f}'.format(raiz_2))

	
