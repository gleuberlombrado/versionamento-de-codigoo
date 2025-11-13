import tkinter as tk
from tkinter import messagebox, ttk

class ControleMarmitasGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🍱 Controle de Marmitas")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        
        self.estoque = {
            'arroz': 0,    
            'feijao': 0,   
            'carne': 0,    
            'salada': 0    
        }
        
        self.porcao_por_marmita = {
            'arroz': 100,
            'feijao': 50,
            'carne': 25,
            'salada': 10
        }

        self._montar_interface()
        self.atualizar_lista_estoque()

   
    def _montar_interface(self):
        titulo = tk.Label(self.root, text="🍱 Controle de Marmitas", font=("Arial", 16, "bold"))
        titulo.pack(pady=10)

        frame = tk.Frame(self.root)
        frame.pack(pady=5)

        tk.Label(frame, text="Ingrediente:").grid(row=0, column=0, padx=5, pady=5)
        self.combo_ingrediente = ttk.Combobox(frame, values=["arroz", "feijao", "carne", "salada"], state="readonly")
        self.combo_ingrediente.current(0)
        self.combo_ingrediente.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="Quantidade (g):").grid(row=1, column=0, padx=5, pady=5)
        self.entry_quantidade = tk.Entry(frame)
        self.entry_quantidade.grid(row=1, column=1, padx=5, pady=5)

        btn_adicionar = tk.Button(frame, text="Adicionar ao estoque", command=self.adicionar_estoque)
        btn_adicionar.grid(row=2, column=0, columnspan=2, pady=10)

        separador = ttk.Separator(self.root, orient='horizontal')
        separador.pack(fill='x', pady=5)

        self.lista_estoque = tk.Listbox(self.root, height=6, font=("Courier", 11))
        self.lista_estoque.pack(fill='both', padx=20, pady=5)

        frame_venda = tk.Frame(self.root)
        frame_venda.pack(pady=10)

        tk.Label(frame_venda, text="Vender marmitas:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_venda = tk.Entry(frame_venda, width=10)
        self.entry_venda.grid(row=0, column=1, padx=5, pady=5)

        btn_vender = tk.Button(frame_venda, text="Vender", bg="#4CAF50", fg="white", command=self.vender_marmita)
        btn_vender.grid(row=0, column=2, padx=5, pady=5)

        self.label_marmitas = tk.Label(self.root, text="Marmitas possíveis: 0", font=("Arial", 12, "bold"))
        self.label_marmitas.pack(pady=10)

    def adicionar_estoque(self):
        ingrediente = self.combo_ingrediente.get()
        try:
            quantidade = float(self.entry_quantidade.get())
            if quantidade <= 0:
                messagebox.showwarning("Aviso", "Digite uma quantidade positiva.")
                return
        except ValueError:
            messagebox.showerror("Erro", "Digite um número válido!")
            return
        
        self.estoque[ingrediente] += quantidade
        messagebox.showinfo("Sucesso", f"{quantidade}g de {ingrediente} adicionados ao estoque.")
        self.entry_quantidade.delete(0, tk.END)
        self.atualizar_lista_estoque()

    def atualizar_lista_estoque(self):
        self.lista_estoque.delete(0, tk.END)
        for ing, qtd in self.estoque.items():
            self.lista_estoque.insert(tk.END, f"{ing.capitalize():8}: {qtd:6.1f} g")
        self.label_marmitas.config(text=f"Marmitas possíveis: {self.calcular_marmitas_possiveis()}")

    def calcular_marmitas_possiveis(self):
        marmitas = []
        for ing, qtd in self.estoque.items():
            if self.porcao_por_marmita[ing] > 0:
                marmitas.append(qtd // self.porcao_por_marmita[ing])
        return int(min(marmitas)) if marmitas else 0

    def vender_marmita(self):
        try:
            qtd = int(self.entry_venda.get())
            if qtd <= 0:
                messagebox.showwarning("Aviso", "Digite uma quantidade válida de marmitas.")
                return
        except ValueError:
            messagebox.showerror("Erro", "Digite um número inteiro válido!")
            return

        marmitas_disp = self.calcular_marmitas_possiveis()
        if qtd > marmitas_disp:
            messagebox.showerror("Erro", f"Não há ingredientes suficientes!\nDisponíveis: {marmitas_disp}")
            return
        
        for ing in self.estoque:
            self.estoque[ing] -= self.porcao_por_marmita[ing] * qtd
        
        messagebox.showinfo("Venda registrada", f"{qtd} marmita(s) vendida(s) com sucesso!")
        self.entry_venda.delete(0, tk.END)
        self.atualizar_lista_estoque()


if __name__ == "__main__":
    root = tk.Tk()
    app = ControleMarmitasGUI(root)
    root.mainloop()