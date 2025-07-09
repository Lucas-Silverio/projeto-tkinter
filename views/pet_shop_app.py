import tkinter as tk
from models.cachorro import Cachorro
from tkinter import messagebox
from tkinter import ttk
import json
from views.cadastro_view import CachorroView

class PetshopApp():
    def __init__(self, master):
        self.master = master
        self.dados = []
        master.title("Lista - Petshop")

        #Titulo
        self.titulo = ttk.Label(master=master, text="Lista de Registros", font=("Arial", 20),foreground="blue")
        self.titulo.grid(row=0,columnspan=3,padx=10,pady=10)

        #Adicionar a lista e configurar
        self.colunas = ('Nome','Raça','Dono','Endereço','Data Cadastro')
        self.lista_cadastrados = ttk.Treeview(master,columns=self.colunas,show="headings",height=20,selectmode="browse")
        self.lista_cadastrados.grid(row=1,columnspan=3,pady=20,padx=10)
        self.vertical_scrollbar = ttk.Scrollbar(master=self.master,orient="vertical",command=self.lista_cadastrados.yview)
        self.vertical_scrollbar.grid(row=1,column=4,padx=0,sticky="ns")
        self.lista_cadastrados.configure(yscrollcommand=self.vertical_scrollbar.set)
        self.construir_lista()

        #Montar botoes 
        self.btn_cadastrar = ttk.Button(master, text="Cadastrar Cachorro", command=self.abrir_janela_cadastro)
        self.btn_cadastrar.grid(row=2,column=0,pady=5,padx=5,sticky="ns")
        self.btn_deletar = ttk.Button(master,text="Deletar Cachorro",command=self.deletar_item)
        self.btn_deletar.grid(row=2,column=1,pady=5,padx=5,sticky="ns")
        self.btn_selecionar = ttk.Button(master,text="Selecionar",command=self.selecionar_item)
        self.btn_selecionar.grid(row=2,column=2,pady=5,padx=5,sticky="ns")

    #Metodos relacionados aos botões
    def abrir_janela_cadastro(self):
        CachorroView(self.master,self)
        self.preencher_lista()
    def deletar_item(self):
        selecionado = self.encontrar_item()
        if selecionado:
            resposta = messagebox.askquestion("Deletar",f"Deseja deletar o registro : Cachorro: {selecionado["item"]["nome"]}, Dono: {selecionado["item"]["nome_dono"]}")
            print(resposta)
            if resposta == "yes":
                for i in self.dados:
                    if(i["nome"] == selecionado["item"]["nome"] and i["nome_dono"] == selecionado["item"]["nome_dono"]):
                        self.dados.pop(selecionado["index"])
                self.atualizar_lista(self.dados)
    def encontrar_item(self):
        selecionado = self.selecionar_item()
        encontrado = {}
        index = 0
        for i in self.dados:
            if i["nome"] == selecionado["nome"] and i["nome_dono"] == selecionado["dono"]:
                encontrado["item"] = i
                encontrado["index"] = index
            index += 1
        return encontrado
    def selecionar_item(self):
        selecionados = self.lista_cadastrados.selection()
        if selecionados:
            for i in selecionados:
                item_data = self.lista_cadastrados.item(i)
                escolhido = {"nome": item_data["values"][0], "dono" : item_data["values"][2]}
                messagebox.showinfo("Selecionado",f"Nome do cachorro: {escolhido['nome']}, Dono: {escolhido['dono']}")
                return escolhido
        else:
            messagebox.showwarning("Não selecionado", "Nenhum item foi selecionado")

    #Metodos relacionados ao Treeview e a lista.
    def atualizar_lista(self,atualizada):
        with open('./dados/dados.json', "w", encoding="utf-8") as f:
            json.dump(atualizada,f,ensure_ascii=True)
        self.preencher_lista()
    def preencher_lista(self):
        self.limpar_lista()
        with open('./dados/dados.json', "r") as f:
                self.dados = json.load(f)
        if self.dados:
            self.construir_lista()
    def limpar_lista(self):
        if self.lista_cadastrados:
            self.lista_cadastrados.delete(*self.lista_cadastrados.get_children())
        else:
            messagebox.showwarning("Lista vazia")
    def construir_lista(self):
        for i in self.colunas:
            self.lista_cadastrados.heading(i, text=i)
        for i in self.dados:
            self.lista_cadastrados.insert("","end",values=(i["nome"],i["raca"],i["nome_dono"],i["endereco"],i["data_cadastro"]))