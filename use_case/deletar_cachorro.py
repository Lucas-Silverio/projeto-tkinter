class DeletarCachorro():
    def __init__(self,repository):
        self.repository = repository
    
    def executar(self,item):
        self.repository.deletar_banco(item)