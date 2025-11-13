nome_completo = input("Digite o seu nome completo: ")
partes_nomes = nome_completo.split()
if len(partes_nomes) >= 2:
    print(partes_nomes[1])
else:
    print("Por favor,digite pelo menos nome e sobrenome. ")
