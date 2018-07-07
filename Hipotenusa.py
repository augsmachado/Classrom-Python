#Encontra a hipotenusa de um triangulo

from math import hypot

opo = float(input('Digite o cateto oposto: '))
adj = float(input('Digite o cateto adjacente: '))

print('A hipotenusa de {} e {} eh {}'.format(opo, adj, hypot(opo,adj)))