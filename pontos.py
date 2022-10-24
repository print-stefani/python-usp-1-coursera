import math

x = int (input ("Digite a coordenada x: "))
x2 = int (input ("Digite a coordenada x2: "))
y = int (input ("Digite a coordenada y: "))
y2 = int (input ("Digite a coordenada y2: "))

d = math.sqrt ((x - x2)**2) + ((y -y2)**2)

if d >= 10:
  print ("longe")
else:
  print ("perto")
