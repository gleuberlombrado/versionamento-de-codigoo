
nome_completo = input("Digite seu nome completo: ")

partes = nome_completo.split()

if len(partes) >= 2:
    
    print("Seu sobrenome é:", partes[1])
else:
    print("Por favor, digite pelo menos nome e sobrenome.")