print("verificador de maior idade itin")

ano_nascimento = int(input("Digite o ano em que você nasceu: "))
ano_atual = 2025

idade = ano_atual - ano_nascimento

if idade == 18:
    print(f"Você fará ou já fez 18 anos em {ano_atual}.")
elif idade > 18:
    anos_passados = idade - 18
    print(f"Você já completou 18 anos")
    print(f"Você tem {idade} anos em {ano_atual}.")
   
else:
    anos_faltando = 18 - idade
    print(f"Você ainda não tem 18 anos")
    print(f"Você tem {idade} anos em {ano_atual}.")
 