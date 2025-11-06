from datetime import datetime
from math import ceil


TARIFA_HORA = 15.00
TARIFA_FRACAO_15_MINUTOS = 3.00
TARIFA_DIARIA = 60
MINUTOS_POR_FRACAO = 15
MINUTOS_POR_HORA = 60
MINUTOS_POR_DIARIA = 24 * MINUTOS_POR_HORA

def calcular_valor_estacionamento(minutos_permanencia):
    """
    Calcula o valor total a ser pago com base no tempo de permanência em minutos,
    aplicando as regras de hora, fração e diária.
    """
    
   
    num_diarias = minutos_permanencia // MINUTOS_POR_DIARIA
    minutos_restantes = minutos_permanencia % MINUTOS_POR_DIARIA
    valor_diarias = num_diarias * TARIFA_DIARIA
    
    
    
    if minutos_restantes == 0:
        valor_restante = 0.00
    elif minutos_restantes <= MINUTOS_POR_HORA:
        
        num_fracoes = ceil(minutos_restantes / MINUTOS_POR_FRACAO)
        valor_restante = num_fracoes * TARIFA_FRACAO_15_MINUTOS
        
    elif minutos_restantes > MINUTOS_POR_HORA:
       
        horas_completas = minutos_restantes // MINUTOS_POR_HORA
        minutos_apos_horas = minutos_restantes % MINUTOS_POR_HORA
        
        valor_horas_completas = horas_completas * TARIFA_HORA
        
        
        num_fracoes = ceil(minutos_apos_horas / MINUTOS_POR_FRACAO)
        valor_fracoes = num_fracoes * TARIFA_FRACAO_15_MINUTOS
        
        valor_restante = valor_horas_completas + valor_fracoes

        
        if valor_restante > TARIFA_DIARIA:
            valor_restante = TARIFA_DIARIA
    
    valor_total = valor_diarias + valor_restante
    return valor_total, num_diarias, minutos_restantes


def entrada_manual_veiculo():
    """Solicita os dados de entrada do veículo ao usuário."""
    print("--- Registro de Entrada ---")
    
    
    placa = input("Digite a placa do carro (Ex: ABC1234): ").upper().strip()
    
   
    while True:
        data_hora_str = input("Digite a data e hora de entrada (Formato DD/MM/AAAA HH:MM): ")
        try:
            data_hora_entrada = datetime.strptime(data_hora_str, '%d/%m/%Y %H:%M')
            break
        except ValueError:
            print("Formato de data e hora inválido. Use DD/MM/AAAA HH:MM.")
            
    
    while True:
        data_hora_saida_str = input("Digite a data e hora de saída (Formato DD/MM/AAAA HH:MM): ")
        try:
            data_hora_saida = datetime.strptime(data_hora_saida_str, '%d/%m/%Y %H:%M')
            
            
            if data_hora_saida < data_hora_entrada:
                print("A hora/data de saída não pode ser anterior à hora/data de entrada. Tente novamente.")
            else:
                break
        except ValueError:
            print("Formato de data e hora inválido. Use DD/MM/AAAA HH:MM.")

    return placa, data_hora_entrada, data_hora_saida


def imprimir_ticket(placa, entrada, saida, valor_total, duracao):
    """Imprime o ticket de estacionamento com todos os detalhes."""
    
    horas, minutos = divmod(duracao.total_seconds() / 60, 60)
    dias, horas_restantes = divmod(horas, 24)
    
   
    tempo_permanencia = ""
    if int(dias) > 0:
        tempo_permanencia += f"{int(dias)} dia(s), "
    tempo_permanencia += f"{int(horas_restantes)} hora(s) e {int(minutos)} minuto(s)"

    print("\n" + "="*40)
    print("      🎫 **TICKET DE ESTACIONAMENTO** 🎫")
    print("="*40)
    print(f"**Placa do Veículo:** {placa}")
    print("-" * 40)
    print(f"**ENTRADA**")
    print(f"  Data: {entrada.strftime('%d/%m/%Y')}")
    print(f"  Hora: {entrada.strftime('%H:%M:%S')}")
    print("-" * 40)
    print(f"**SAÍDA**")
    print(f"  Data: {saida.strftime('%d/%m/%Y')}")
    print(f"  Hora: {saida.strftime('%H:%M:%S')}")
    print("-" * 40)
    print(f"**Tempo de Permanência:** {tempo_permanencia}")
    print("-" * 40)
    print(f"**VALOR TOTAL COBRADO:** R$ {valor_total:.2f}")
    print("="*40)


def simular_estacionamento():
    """Função principal para rodar a simulação."""
    
    placa, entrada, saida = entrada_manual_veiculo()
    
    
    duracao = saida - entrada
    minutos_permanencia = duracao.total_seconds() / 60
    
    if minutos_permanencia <= 0:
        print("\nO tempo de permanência é zero ou negativo. Nenhum valor a ser cobrado.")
        return
        
    valor_total, num_diarias, minutos_restantes = calcular_valor_estacionamento(int(minutos_permanencia))
    
   
    imprimir_ticket(placa, entrada, saida, valor_total, duracao)


if __name__ == "__main__":
    simular_estacionamento()