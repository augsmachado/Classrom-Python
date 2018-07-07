a,b,c = input().split(" ")

a = float(a)
b = float(b)
c = float(c)

"""Teste para saber se eh um triangulo"""
if(abs(b-c)<a<(b+c)) and (abs(a-c)<b<(a+c)) and (abs(a-b)<c<(a+b)):
    print('Perimetro = {}'.format(a+b+c))
else:
    print('Area = {}'.format((c*(a+b))/2))
