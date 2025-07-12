from model.cachorro import Cachorro
class AtualizarCachorro():
    def __init__(self,repository):
        self.repository = repository
    
    def atualizar_cachorro(self,antigo,novo):
        novo.append(antigo["id"])
        novo = Cachorro(*novo)
        novo.data_cadastro = antigo["data_cadastro"]
        self.repository.atualizar_banco(antigo,novo)