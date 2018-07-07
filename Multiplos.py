a,b = input().split(" ")

a = int(a)
b = int(b)

if((a%b == 0) or (b%a == 0)):  #se for multiplo, o resto tem de ser zero
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
