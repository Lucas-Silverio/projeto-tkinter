class BuscarCachorro():
    def __init__(self,repository):
        self.repository = repository

    def execute(self,id):
        encontrado = self.repository.buscar_banco(int(id))
        return encontrado
    def busca_todos(self):
        todos = self.repository.buscar_todos_banco()
        return todos