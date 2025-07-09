import tkinter as tk
from tkinter import messagebox
from models.cachorro import Cachorro
from tkinter import ttk

class CachorroView(tk.Toplevel):
    def __init__(self,master,parent):
        super().__init__()
        self.master = master
        self.parent = parent
        self.title('Cadastro')
        self.geometry('315x450')
        self.resizable(False,False)

        #Configuração Modal
        self.transient(self.master)
        self.grab_set()

        #Customização
        self.fonte_label = ("Arial", 10, "bold")
        self.fonte_entry = ("Arial", 10)
        self.padding_x = 10
        self.padding_y = 5
        self.criar_widgets()

        #Criação dos botões
        btn_cadastrar = ttk.Button(master=self,text="Cadastrar",command=self.cadastrar_cachorro,width=20)
        btn_cadastrar.grid(row=(len(self.campos)),column=0,padx=5,pady=10,sticky="ns")
        btn_cancelar = ttk.Button(master=self,text="Cancelar",command=self.cancelar_cadastro,width=20)
        btn_cancelar.grid(row=(len(self.campos)),column=1,padx=5,pady=10,sticky="ns")
    
    #Metodos relacionados aos botões e widgets
    def criar_widgets(self):
        self.campos = [
            ("Nome do Cachorro:", "nome_cachorro_entry"),
            ("Cor:", "cor_entry"),
            ("Idade:", "idade_entry"),
            ("Raça:", "raca_entry"),
            ("Peso (kg):", "peso_entry"),
            ("Nome do Dono:", "nome_dono_entry"),
            ("CPF do Dono:", "cpf_dono_entry"),
            ("Endereço:", "endereco_entry"),
            ("Número:", "numero_entry"),
            ("Bairro:", "bairro_entry"),
            ("Cidade:", "cidade_entry"),
            ("CEP:", "cep_entry"),
        ]
        self.entries = {}
        for i, (texto, nome_entry) in enumerate(self.campos):
            label = ttk.Label(self, text=texto, font=self.fonte_label)
            label.grid(row=i, column=0, padx=self.padding_x, pady=self.padding_y, sticky="w")
            entry = ttk.Entry(self, font=self.fonte_entry)
            entry.grid(row=i, column=1, padx=self.padding_x, pady=self.padding_y, sticky="ew")
            self.entries[nome_entry] = entry
    def cadastrar_cachorro(self):
        try:
            nome = self.entries["nome_cachorro_entry"].get()
            cor = self.entries["cor_entry"].get()
            idade = int(self.entries["idade_entry"].get())
            raca = self.entries["raca_entry"].get()
            peso = float(self.entries["peso_entry"].get())
            dono = self.entries["nome_dono_entry"].get()
            cpf_dono = self.entries["cpf_dono_entry"].get()
            endereco = self.entries["endereco_entry"].get()
            numero = self.entries["numero_entry"].get()
            bairro = self.entries["bairro_entry"].get()
            cidade = self.entries["cidade_entry"].get()
            cep = self.entries["cep_entry"].get()

            # Validação básica de campos
            if not all([nome, cor, raca, dono, cpf_dono, endereco, numero, bairro, cidade, cep]):
                messagebox.showwarning("Campos Vazios", "Por favor, preencha todos os campos.")
                return

            cachorro = Cachorro(nome, cor, idade, raca, peso, dono, cpf_dono, endereco, numero, bairro, cidade, cep)
            cachorro.salvar_cadastro(dados=self.parent.dados)
            messagebox.showinfo("Cadastro Concluído", f"Cachorro {nome} cadastrado com sucesso!")
            self.parent.preencher_lista()
            self.limpar_campos()

        except ValueError:
            messagebox.showerror("Erro de Entrada", "Por favor, insira valores válidos para Idade (número inteiro) e Peso (número decimal).")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")
    def cancelar_cadastro(self):
        self.destroy()
    def limpar_campos(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)