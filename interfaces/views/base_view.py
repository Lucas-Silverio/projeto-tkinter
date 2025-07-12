from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import Toplevel ,ttk

class BaseView(Toplevel,ABC):
    def __init__(self,master):
        super().__init__(master)
        self.master = master
        self.title('Base')
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
        self.btn_enviar = ttk.Button(master=self,text="Enviar",command=self.enviar,width=20)
        self.btn_enviar.grid(row=(len(self.campos)),column=0,padx=5,pady=10,sticky="ns")
        self.btn_cancelar = ttk.Button(master=self,text="Cancelar",command=self.cancelar_cadastro,width=20)
        self.btn_cancelar.grid(row=(len(self.campos)),column=1,padx=5,pady=10,sticky="ns")
    
    #Metodos relacionados aos botões e widgets
    def criar_widgets(self):
        self.campos = [
            ("Nome do Cachorro:", "nome_entry"),
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

    @abstractmethod
    def enviar(self):
        pass
    def cancelar_cadastro(self):
        self.destroy()
    def limpar_campos(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)