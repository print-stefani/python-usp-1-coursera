segundos = input ("Por favor, entre com o número de segundos que deseja converter:")

total= int(segundos)

dias = total // 86400
horas = dias % 3600
segs_restantes = total % 3600
minutos =segs_restantes // 60
segs_restantes_final = segs_restantes % 60

print(dias, "Dias,", horas, "horas, ",  minutos, "minutos e", segs_restantes_final, "segundos.")
