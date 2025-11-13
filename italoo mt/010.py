numeros = [3,7,12,18,25,31,42,56,63,77]
print("lista de numeros:",numeros)
numero_usuario = int(input("digite um numero para verificar se esta na lista:"))
if numero_usuario in numeros:
    print(f"O numero {numero_usuario} esta na lista!")
else:
    print(f"O numero{numero_usuario} Nao esta na lista.")