import tkinter as tk
from tkinter import ttk, messagebox

class ControleMarmitas:
    def __init__(self):
        self.estoque = {
            'arroz': 0,    # em gramas
            'feijao': 0,   # em gramas
            'carne': 0,    # em gramas
            'salada': 0    # em gramas
        }
        
        # Quantidade necessária por marmita (em gramas)
        self.porcao_por_marmita = {
            'arroz': 100,
            'feijao': 50,
            'carne': 25,
            'salada': 10
        }
    
    def adicionar_estoque(self, ingrediente, quantidade):
        """Adiciona quantidade ao estoque do ingrediente especificado"""
        if ingrediente in self.estoque:
            self.estoque[ingrediente] += quantidade
            print(f"Adicionado {quantidade}g de {ingrediente}. Estoque atual: {self.estoque[ingrediente]}g")
        else:
            print("Ingrediente inválido!")
    
    def verificar_estoque(self):
        """Mostra o estoque atual de todos os ingredientes"""
        print("\n=== ESTOQUE ATUAL ===")
        for ingrediente, quantidade in self.estoque.items():
            print(f"{ingrediente.capitalize()}: {quantidade}g")
    
    def calcular_marmitas_possiveis(self):
        """Calcula quantas marmitas podem ser feitas com o estoque atual"""
        marmitas_possiveis = []
        for ingrediente, quantidade in self.estoque.items():
            if self.porcao_por_marmita[ingrediente] > 0:
                marmitas = quantidade // self.porcao_por_marmita[ingrediente]
                marmitas_possiveis.append(marmitas)
        
        if not marmitas_possiveis:
            return 0
        return min(marmitas_possiveis)
    
    def vender_marmita(self, quantidade):
        """Registra a venda de uma quantidade de marmitas"""
        marmitas_possiveis = self.calcular_marmitas_possiveis()
        
        if quantidade <= 0:
            print("Quantidade inválida!")
            return False
            
        if quantidade > marmitas_possiveis:
            print(f"Não há ingredientes suficientes. Só é possível fazer {marmitas_possiveis} marmita(s).")
            return False
        
        # Atualiza o estoque
        for ingrediente in self.estoque:
            self.estoque[ingrediente] -= self.porcao_por_marmita[ingrediente] * quantidade
        
        print(f"\n✅ {quantidade} marmita(s) vendida(s) com sucesso!")
        print(f"Marmitas restantes possíveis: {self.calcular_marmitas_possiveis()}")
        return True

class AplicacaoMarmitas:
    def __init__(self, root):
        self.root = root
        self.root.title("Controle de Marmitas")
        self.root.geometry("600x500")
        
        self.sistema = ControleMarmitas()
        
        # Criar abas
        self.abas = ttk.Notebook(root)
        self.abas.pack(expand=1, fill='both')
        
        # Aba de Estoque
        self.aba_estoque = ttk.Frame(self.abas)
        self.abas.add(self.aba_estoque, text='Estoque')
        
        # Aba de Vendas
        self.aba_vendas = ttk.Frame(self.abas)
        self.abas.add(self.aba_vendas, text='Vender')
        
        # Aba de Relatório
        self.aba_relatorio = ttk.Frame(self.abas)
        self.abas.add(self.aba_relatorio, text='Relatório')
        
        self.criar_aba_estoque()
        self.criar_aba_vendas()
        self.criar_aba_relatorio()
    
    def criar_aba_estoque(self):
        # Frame para adicionar itens
        frame_adicionar = ttk.LabelFrame(self.aba_estoque, text="Adicionar ao Estoque")
        frame_adicionar.pack(padx=10, pady=5, fill='x')
        
        # Variáveis para os campos de entrada
        self.ingrediente_var = tk.StringVar()
        self.quantidade_var = tk.DoubleVar()
        
        # Dropdown para seleção do ingrediente
        ttk.Label(frame_adicionar, text="Ingrediente:").grid(row=0, column=0, padx=5, pady=5)
        ingredientes = [('Arroz', 'arroz'), ('Feijão', 'feijao'), 
                       ('Carne', 'carne'), ('Salada', 'salada')]
        for i, (text, value) in enumerate(ingredientes):
            rb = ttk.Radiobutton(frame_adicionar, text=text, variable=self.ingrediente_var, 
                               value=value)
            rb.grid(row=0, column=i+1, padx=5, pady=5, sticky='w')
        
        # Campo para quantidade
        ttk.Label(frame_adicionar, text="Quantidade (g):").grid(row=1, column=0, padx=5, pady=5)
        ttk.Entry(frame_adicionar, textvariable=self.quantidade_var, width=10).grid(row=1, column=1, padx=5, pady=5)
        
        # Botão para adicionar
        ttk.Button(frame_adicionar, text="Adicionar ao Estoque", command=self.adicionar_estoque_gui).grid(
            row=2, column=0, columnspan=5, pady=10)
        
        # Área de visualização do estoque
        frame_visualizar = ttk.LabelFrame(self.aba_estoque, text="Estoque Atual")
        frame_visualizar.pack(padx=10, pady=5, fill='both', expand=True)
        
        self.texto_estoque = tk.Text(frame_visualizar, height=10, width=50)
        self.texto_estoque.pack(padx=5, pady=5, fill='both', expand=True)
        self.atualizar_estoque_gui()
    
    def criar_aba_vendas(self):
        # Frame para vender marmitas
        frame_vender = ttk.LabelFrame(self.aba_vendas, text="Vender Marmitas")
        frame_vender.pack(padx=10, pady=5, fill='x')
        
        # Campo para quantidade de marmitas
        ttk.Label(frame_vender, text="Quantidade de Marmitas:").pack(pady=5)
        self.quantidade_venda_var = tk.IntVar()
        ttk.Entry(frame_vender, textvariable=self.quantidade_venda_var, width=10).pack(pady=5)
        
        # Botão para vender
        ttk.Button(frame_vender, text="Registrar Venda", command=self.vender_marmita_gui).pack(pady=10)
        
        # Área de informações
        self.info_venda = ttk.Label(self.aba_vendas, text="teste")
        self.info_venda.pack(pady=5)
    
    def criar_aba_relatorio(self):
        # Área de relatório
        frame_relatorio = ttk.LabelFrame(self.aba_relatorio, text="Relatório de Estoque")
        frame_relatorio.pack(padx=10, pady=5, fill='both', expand=True)
        
        self.texto_relatorio = tk.Text(frame_relatorio, height=15, width=50)
        self.texto_relatorio.pack(padx=5, pady=5, fill='both', expand=True)
        self.atualizar_relatorio()
    
    def adicionar_estoque_gui(self):
        ingrediente = self.ingrediente_var.get()
        quantidade = self.quantidade_var.get()
        
        if not ingrediente:
            messagebox.showwarning("Aviso", "Selecione um ingrediente!")
            return
            
        if quantidade <= 0:
            messagebox.showwarning("Aviso", "A quantidade deve ser maior que zero!")
            return
            
        self.sistema.adicionar_estoque(ingrediente, quantidade)
        messagebox.showinfo("Sucesso", f"Adicionado {quantidade}g de {ingrediente} ao estoque!")
        self.atualizar_estoque_gui()
        self.atualizar_relatorio()
        self.quantidade_var.set(0)
    
    def vender_marmita_gui(self):
        try:
            quantidade = self.quantidade_venda_var.get()
            if quantidade <= 0:
                messagebox.showwarning("Aviso", "A quantidade deve ser maior que zero!")
                return
                
            if self.sistema.vender_marmita(quantidade):
                messagebox.showinfo("Sucesso", f"Venda de {quantidade} marmita(s) registrada!")
                self.atualizar_estoque_gui()
                self.atualizar_relatorio()
                self.quantidade_venda_var.set(0)
        except ValueError:
            messagebox.showerror("Erro", "Digite um número válido!")
    
    def atualizar_estoque_gui(self):
        self.texto_estoque.config(state='normal')
        self.texto_estoque.delete(1.0, tk.END)
        
        for ingrediente, quantidade in self.sistema.estoque.items():
            self.texto_estoque.insert(tk.END, f"{ingrediente.capitalize()}: {quantidade}g\n")
        
        self.texto_estoque.config(state='disabled')
    
    def atualizar_relatorio(self):
        self.texto_relatorio.config(state='normal')
        self.texto_relatorio.delete(1.0, tk.END)
        
        marmitas_possiveis = self.sistema.calcular_marmitas_possiveis()
        self.texto_relatorio.insert(tk.END, f"=== RELATÓRIO DE ESTOQUE ===\n\n")
        self.texto_relatorio.insert(tk.END, f"Marmitas possíveis: {marmitas_possiveis}\n\n")
        
        for ingrediente, quantidade in self.sistema.estoque.items():
            porcao = self.sistema.porcao_por_marmita[ingrediente]
            porcoes = quantidade // porcao if porcao > 0 else 0
            self.texto_relatorio.insert(tk.END, 
                f"{ingrediente.capitalize()}: {quantidade}g (suficiente para {porcoes} marmitas)\n")
        
        self.texto_relatorio.config(state='disabled')

def main():
    root = tk.Tk()
    app = AplicacaoMarmitas(root)
    root.mainloop()

if __name__ == "__main__":
    main()
