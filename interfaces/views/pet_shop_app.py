from tkinter import messagebox
from tkinter import ttk

class PetshopApp():
    def __init__(self, master,pet_shop_vm):
        self.master = master
        #viewModel interação de dados referentes a pet_shop_view
        self.pet_shop_vm = pet_shop_vm
        self.lista = self.pet_shop_vm.carregar_lista()
        
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
        self.btn_selecionar = ttk.Button(master,text="Selecionar", command=self.abrir_janela_atualizar)
        self.btn_selecionar.grid(row=2,column=2,pady=5,padx=5,sticky="ns")

    def abrir_janela_atualizar(self):
        selecionado = self.encontrar_item()
        if selecionado:
            self.pet_shop_vm.abrir_janela_atualizar(self.master,selecionado)
            self.preencher_lista()
    #Metodos relacionados aos botões
    def abrir_janela_cadastro(self):
        self.pet_shop_vm.abrir_janela_cadastro(self.master)
        self.preencher_lista()
    #Chama minha view_model para deletar item selecionado e atualizar a lista
    def deletar_item(self):
        selecionado = self.encontrar_item()
        if selecionado:
            resposta = messagebox.askquestion("Deletar",f"Deseja deletar o registro : Cachorro: {selecionado["nome"]}, Dono: {selecionado["nome_dono"]}")
            if resposta == "yes":
                self.pet_shop_vm.deletar_cachorro_uc(selecionado)
                messagebox.showinfo("Deletado","Deletado com sucesso.")
                self.preencher_lista()
    #Chama minha view_model para usar o caso de uso e buscar selecionado 
    def encontrar_item(self):
        selecionado = self.lista_cadastrados.focus()
        if selecionado != "":
            encontrado = self.pet_shop_vm.buscar_cachorro_uc(selecionado)
            return encontrado
        else:
            messagebox.showwarning("Não selecionado","Por favor selecione um registro")
    #Metodos relacionados ao Treeview e a lista.
    def preencher_lista(self):
        self.limpar_lista()
        self.lista = self.pet_shop_vm.carregar_lista()
        self.construir_lista()
    def limpar_lista(self):
        if self.lista_cadastrados:
            self.lista_cadastrados.delete(*self.lista_cadastrados.get_children())
        else:
            messagebox.showwarning("Lista vazia")
    def construir_lista(self):
        for i in self.colunas:
            self.lista_cadastrados.heading(i, text=i)
        for i in self.lista:
            self.lista_cadastrados.insert("","end",iid=i["id"],values=(i["nome"],i["raca"],i["nome_dono"],i["endereco"],i["data_cadastro"]))