from model.cachorro import Cachorro
class SalvarCachorro():
    def __init__(self, repository):
        self.repository = repository
    
    def salvar(self,campos):
        novo = Cachorro(*campos)
        if novo:
            lista = self.repository.buscar_todos_banco()
            if len(lista) >= 1:
                novo.id = lista[-1]["id"] + 1
        self.repository.salvar_banco(novo)