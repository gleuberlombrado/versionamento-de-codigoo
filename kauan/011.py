print("=== SISTEMA DE ESTACIONAMENTO ===")

placa = input("Digite a placa do carro: ")
dataEntrada = input("Data de entrada (DD/MM/AAAA): ")
horaEntrada = int(input("Hora de entrada: "))
minEntrada = int(input("Minutos de entrada: "))

dataSaida = input("Data de saída (DD/MM/AAAA): ")
horaSaida = int(input("Hora de saída: "))
minSaida = int(input("Minutos de saída: "))


totalMin = (horaSaida * 60 + minSaida) - (horaEntrada * 60 + minEntrada)

if totalMin <= 0:
    print("Erro no horário. A saída não pode ser antes da entrada.")
else:
    
    if totalMin >= 480:
        valor = 60.00
    else:
        horas = totalMin // 60
        restoMin = totalMin % 60

       
        fracoes = restoMin // 15
        if restoMin % 15 > 0:
            fracoes += 1
        
        valor = horas * 12 + fracoes * 3

    print("\n===== TICKET =====")
    print("Placa:", placa)
    print("Entrada:", dataEntrada, "-", f"{horaEntrada:02d}:{minEntrada:02d}")
    print("Saída:", dataSaida, "-", f"{horaSaida:02d}:{minSaida:02d}")
    print("Tempo total:", totalMin, "minutos")
    print("Valor a pagar: R$", round(valor, 2))