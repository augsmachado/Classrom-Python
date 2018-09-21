# determinar o tipo de triangulo que os tres lados formam
from math import pow

x = list(map(float, input().split(" ")))

x.sort()
x.reverse()

if (x[0] >= (x[1]+x[2])):
    print('NAO FORMA TRIANGULO')
elif (pow(x[0],2) == (pow(x[1],2)+pow(x[2],2))):
    print('TRIANGULO RETANGULO')
elif (pow(x[0],2) > (pow(x[1],2)+pow(x[2],2))):
    print('TRIANGULO OBTUSANGULO')

    if ((x[0] == x[1] and x[0] != x[2]) or (x[1] == x[2] and x[1] != x[0]) or (x[2] == x[0] and x[2] != x[1])):
        print('TRIANGULO ISOSCELES')
    elif (x[0] == x[1] == x[2]):
        print('TRIANGULO EQUILATERO')

elif (pow(x[0], 2) < (pow(x[1], 2) + pow(x[2], 2))):
    print('TRIANGULO ACUTANGULO')

    if ((x[0] == x[1] and x[0] != x[2]) or (x[1] == x[2] and x[1] != x[0]) or (x[2] == x[0] and x[2] != x[1])):
        print('TRIANGULO ISOSCELES')
    elif (x[0] == x[1] == x[2]):
        print('TRIANGULO EQUILATERO')
