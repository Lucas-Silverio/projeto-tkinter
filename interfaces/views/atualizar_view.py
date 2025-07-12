from interfaces.views.base_view import BaseView
from tkinter import messagebox
class AtualizarView(BaseView):
    def __init__(self,master,att_cachorro_uc,selecionado):
        super().__init__(master)
        self.master = master
        self.att_cachorro_uc = att_cachorro_uc
        self.selecionado = selecionado
        self.title("Atualizar")
        self.btn_enviar.configure(text="Atualizar")
        self.preencher_campos()
    
    def enviar(self):
        try:
            campos = []
            for i in self.entries:
                if i == "idade_entry":
                    campos.append(self.entries[i].get())
                elif i == "peso_entry":
                    campos.append(self.entries[i].get())
                else:
                    campos.append(self.entries[i].get())
            self.att_cachorro_uc.atualizar_cachorro(self.selecionado,campos)
        except ValueError as erro:
            messagebox.showerror("Ação inválida",erro)
            
    def preencher_campos(self):
        self.botoes = self.entries
        for i in self.botoes:
            campo = i.replace("_entry","")
            self.botoes[i].insert(0, self.selecionado[campo])