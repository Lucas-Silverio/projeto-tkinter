from interfaces.views.cadastro_view import CadastroView
from interfaces.views.atualizar_view import AtualizarView

class PetShopVM():
    def __init__(self,sv_cachorro_uc,del_cachorro_uc,bsc_cachorro_uc,att_cachorro_uc):
        self.bsc_cachorro_uc = bsc_cachorro_uc
        self.del_cachorro_uc = del_cachorro_uc
        self.sv_cachorro_uc = sv_cachorro_uc
        self.att_cachorro_uc = att_cachorro_uc
    
    def carregar_lista(self):
        self.dados = self.bsc_cachorro_uc.busca_todos()
        return self.dados
    
    def abrir_janela_cadastro(self,master):
        cad_view = CadastroView(master,self.sv_cachorro_uc)
        cad_view.wait_window()
        self.carregar_lista()
        
    def abrir_janela_atualizar(self,master,selecionado):
        att_view = AtualizarView(master,self.att_cachorro_uc,selecionado)
        att_view.wait_window()
        self.carregar_lista()

    def buscar_cachorro_uc(self,id):
        return self.bsc_cachorro_uc.execute(int(id))
    def deletar_cachorro_uc(self,selecionado):
        try:
            self.del_cachorro_uc.executar(selecionado)
            self.carregar_lista()
        except Exception as e:
            print("erro: ",e)