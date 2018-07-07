n=input('Digite algo ')

print(type(n)) #qual o tipo da variavel digitada
print('Eh um numero: {}'.format(n.isnumeric()))  #eh um numero
print('Eh uma letra: {}'.format(n.isalpha()))  #eh uma letra
print('Eh um alfa-numerico: {}'.format(n.isalnum()))  #eh um alfa-numerico
