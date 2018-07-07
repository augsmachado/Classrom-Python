# determinar o tipo de triangulo que os tres lados formam
from math import pow
a,b,c = input().split(" ")

a = float(a)
b = float(b)
c = float(c)

if (a>b and a> c):
    if (b < c):
        aux = b
        b = c
        c = aux
elif (b>a  and b>c):
    aux = a
    a = b
    b = aux
    if (b < c):
        aux = b
        b = c
        c = aux
elif (c > a and c > b):
    aux = a
    a = c
    c = aux
    if (b < c):
        aux = b
        b = c
        c = aux

if (a >= (b+c)):
    print('NAO FORMA TRIANGULO')
else:
    if (pow(a,2) == (pow(b,2)+pow(c,2))):
        print('TRIANGULO RETANGULO')
    elif (pow(a,2) > (pow(b,2)+pow(c,2))):
        print('TRIANGULO OBTUSANGULO')
    elif (pow(a,2) < (pow(b,2)+pow(c,2))):
        print('TRIANGULO ACUTANGULO')
    
    if (a == b == c):
        print('TRIANGULO EQUILATERO')
    else:
        print('TRIANGULO ISOCELES')
