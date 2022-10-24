lar = int(input('digite a largura: '))
alt = int(input('digite a altura: '))

coluna = 1 
linha = 1

while linha <= alt:
   print('#' * lar, end = "")
   print() 
   linha += 1
   
   while linha > 1 and linha < alt:
      print('#' + ' ' * (lar - 2) + '#')
      linha += 1
      break
