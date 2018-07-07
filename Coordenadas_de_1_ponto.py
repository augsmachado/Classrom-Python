#Entradas multiplas de um numero
x,y = input().split(" ")

#Conversao de Str para float
x = float (x)
y = float(y)

#De acordo com as coordenadas, diz onde o ponto estah
if ((x == 0.) and (y == 0.)):
    print('Origem')
elif (x == 0.):
    print('Eixo Y')
elif (y == 0.):
    print('Eixo X')
else:
    if(x > 0.):
        if (y > 0.):
            print('Q1')
        else:
            print('Q4')
    else:
        if (y > 0.):
            print('Q2')
        else:
            print('Q3\n') 
