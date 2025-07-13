import tkinter as tk
from interfaces.views.pet_shop_app import PetshopApp
from interfaces.view_model.pet_shop_view_model import PetShopVM
from dados.repository_simulado import Repository
from use_case import (atualizar_cachorro, deletar_cachorro,buscar_cachorro,salvar_cachorro)

def centralizar_tela(root,largura,altura):
    tela_largura = root.winfo_screenwidth()
    tela_altura = root.winfo_screenheight()
    #centralizar
    x = (tela_largura // 2) - (largura // 2)
    y = (tela_altura // 2) - (altura // 2)
    root.geometry(f"{largura}x{altura}+{x}+{y}")

if __name__ == "__main__":
    #repository
    repository = Repository()
    #usecase
    sv_cachorro_uc = salvar_cachorro.SalvarCachorro(repository)
    del_cachorro_uc = deletar_cachorro.DeletarCachorro(repository)
    bsc_cachorro_uc = buscar_cachorro.BuscarCachorro(repository)
    att_cachorro_uc = atualizar_cachorro.AtualizarCachorro(repository)
    #viewModel
    view_model_pet = PetShopVM(sv_cachorro_uc,del_cachorro_uc,bsc_cachorro_uc,att_cachorro_uc)
    #main
    root = tk.Tk()
    root.resizable(False,False)
    #view
    app = PetshopApp(root,view_model_pet)
    centralizar_tela(root,1050,600)
    root.mainloop()