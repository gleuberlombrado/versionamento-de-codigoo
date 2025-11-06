numeros = [3, 7, 10, 15, 22, 31, 45, 50]

print("Lista de números:", numeros)

numero_usuario = int(input("Digite um número para verificar: "))

if numero_usuario in numeros:
    print("✅ O número está na lista!")
else:
    print("❌ O número não está na lista.")