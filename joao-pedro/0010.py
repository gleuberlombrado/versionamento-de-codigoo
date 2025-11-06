numeros = [2, 5, 8, 12, 16, 19, 23, 27, 32]
num_usuario = int(input("Digite um número para verificar se está na lista: "))
if num_usuario in numeros:
    print(f"O número {num_usuario} está na lista!")
else:
    print(f"O número {num_usuario} NÃO está na lista.")