from datetime import datetime

class Estacionamento:
    def __init__(self):
        self.veiculos = {}
        self.valor_hora = 12.00
        self.valor_fracao = 3.00
        self.valor_diaria = 60.00

    def entrada(self, placa, data_str, hora_str):
        entrada = datetime.strptime(f"{data_str} {hora_str}", "%d/%m/%Y %H:%M")
        self.veiculos[placa] = entrada
        print(f"Entrada registrada para {placa}")

    def saida(self, placa, data_str, hora_str):
        if placa not in self.veiculos:
            return "Veículo não encontrado!"
        
        entrada = self.veiculos[placa]
        saida = datetime.strptime(f"{data_str} {hora_str}", "%d/%m/%Y %H:%M")
        tempo = saida - entrada
        
        if tempo.days >= 1:
            valor = (tempo.days * self.valor_diaria) + ((tempo.seconds // 3600) * self.valor_hora)
        else:
            horas = tempo.seconds // 3600
            minutos = (tempo.seconds % 3600) // 60
            fracao = (minutos + 14) // 15
            valor = (horas * self.valor_hora) + (fracao * self.valor_fracao)
            valor = min(valor, self.valor_diaria)

        print("\n" + "="*50)
        print(f"Placa: {placa}")
        print(f"Entrada: {entrada.strftime('%d/%m/%Y %H:%M')}")
        print(f"Saída: {saida.strftime('%d/%m/%Y %H:%M')}")
        print(f"Tempo: {str(tempo).split('.')[0]}")
        print(f"Valor: R$ {max(3.00, valor):.2f}")
        print("="*50 + "\n")
        
        del self.veiculos[placa]

if __name__ == "__main__":
    est = Estacionamento()
    while True:
        print("\n1. Registrar entrada\n2. Registrar saída\n3. Sair")
        op = input("Opção: ")
        
        if op == '1':
            placa = input("Placa: ").upper()
            data = input("Data (DD/MM/AAAA): ")
            hora = input("Hora (HH:MM): ")
            est.entrada(placa, data, hora)
        elif op == '2':
            placa = input("Placa: ").upper()
            data = input("Data (DD/MM/AAAA): ")
            hora = input("Hora (HH:MM): ")
            est.saida(placa, data, hora)
        elif op == '3':
            break