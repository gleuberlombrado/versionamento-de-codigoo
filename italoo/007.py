cidades = []

while True:
    nome = input("digite o nome de uma cidade(ou 'sair' para encerrar):")

    if nome.lower()=='sair':
        print("programa encerrado.")
        break

    cidades.append(nome)

    print("lista de cidades atualizada:")
    for cidade in cidades:
        print("-", cidade)