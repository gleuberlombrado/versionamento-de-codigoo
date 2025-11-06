import random
while True:
   lista_aleatoria = [random.randint(1, 100) for _ in range(10)]
   print("os lista_aleatoria de 1 a 100 foram gerados")
   numero = int(input("Digite um número para verificar se está na lista: "))
   if numero in lista_aleatoria:
    print(f"O número {numero} está na lista! ")
    print("a lista de numero era:", lista_aleatoria)
   else:
    print(f"O número {numero} NÃO está na lista. ")
    