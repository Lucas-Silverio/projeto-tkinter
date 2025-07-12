import os
import json
from model.cachorro import Cachorro
class Repository():
    def __init__(self):
        self.dados = self.buscar_todos_banco()
        if not os.path.exists('./dados/dados.json'):
            with open('./dados/dados.json', 'w',encoding='utf-8') as f:
                json.dump(self.dados,f,ensure_ascii=True)

    def salvar_banco(self,novo):
        self.dados.append(novo.to_dict())
        self.atualizar_lista_banco(self.dados)

    def atualizar_lista_banco(self,dados):
        with open('./dados/dados.json', 'w',encoding="utf-8") as f:
            json.dump(dados,f,ensure_ascii=True)

    def buscar_banco(self,id):
        encontrado = None
        for item in self.dados:
            if item["id"] == id:
                encontrado = item
        return encontrado
    
    def deletar_banco(self,item):
        if item:
            for i,x in enumerate(self.dados):
                if item["id"] == x["id"]:
                    self.dados.pop(i)
                    self.atualizar_lista_banco(self.dados)

    def buscar_todos_banco(self):
        try:
            with open('./dados/dados.json' , 'r', encoding='utf-8') as f:
                self.dados = json.load(f)
            return self.dados
        except Exception as e:
            print("Lista vazia ou com erro: ",e)
        return []
    
    def atualizar_banco(self,antigo,novo):
        if antigo and novo:
            self.deletar_banco(antigo)
            self.dados.append(novo.to_dict())
            self.atualizar_lista_banco(self.dados)
