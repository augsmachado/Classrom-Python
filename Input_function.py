#Entrada de texto
print("Hi, I'm Python. What's your name?")
name = input()
print("Hello,",name,"- nice to meet you!")

#Entrada de múltiplas variáveis na mesma linha
a, b = input().split()

a = int(a)
b = int(b)

print("Resultado: {:.2}".format(a/b))
