nome_completo = input("Digite seu nome completo: ")
partes = nome_completo.split()
if len(partes) >= 2:
    print(partes[1])
else:
    print("Você precisa digitar pelo menos dois nomes.")