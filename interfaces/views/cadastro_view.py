from tkinter import messagebox
from interfaces.views.base_view import BaseView

class CadastroView(BaseView):
    def __init__(self,master,sv_cachorro_uc):
        super().__init__(master)
        self.master = master
        self.sv_cachorro_uc = sv_cachorro_uc
        self.title('Cadastro')
        
        #Criação dos botões
        self.btn_enviar.configure(text="Cadastrar")

    def enviar(self):
        campos = []
        try:
            for i in self.entries:
                campos.append(self.entries[i].get())
            self.sv_cachorro_uc.salvar(campos)
            self.limpar_campos()
        except ValueError as erro:
            messagebox.showwarning("Valores inválidos",erro)
        