
#leitura das posições
face_1 = [int (i) for i in input().split()]
face_2 = [int (i) for i in input().split()]
face_3 = [int (i) for i in input().split()]


total = len (face_1 or face_2 or face_3)

soma = 0

for i in range (total):
  total_1 = face_1 .count (1)
  total_2 = face_2 .count (1)
  total_3 = face_3 .count (1)
  soma = total_1 + total_2 + total_3
print (soma)
