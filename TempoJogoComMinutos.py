h1, min1, h2, min2 = input().split()

h1 = int(h1)
min1 = int(min1)
h2 = int(h2)
min2 = int(min2)

horas = 0
minutos = 0
if h1 == h2:
    if min1 == min2:
        horas = 24
    else:
        if min1 > min2:
            horas = 23
            minutos = (60 - min1) + min2
        else:
            horas = h1 - h2
            minutos = min2 - min1
else:
    if min1 > min2:
        minutos = (60 - min1) + min2
    else:
        minutos = min2 - min1

    if h1 > h2:
        horas = (24 - h1) + h2
    elif h2 > h1:
        if min1 < min2 or min1 == min2:
            horas = h2 - h1
    
print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(horas, minutos))
