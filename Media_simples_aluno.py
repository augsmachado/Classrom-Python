#Calcula a media de um aluno
n1 = float(input('Digite sua 1 nota:'))
n2 = float(input('Digite sua 2 nota: '))

media = (n1+n2)/2

if media>=5:
    print('Sua media foi {:.1f}, parabens'.format(media))
else:
    print('Sua media foi {:.1f}, precisa melhorar'.format(media))
