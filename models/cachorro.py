import datetime
import os
import json

class Cachorro:
    def __init__(self, nome, cor, idade, raca, peso, dono, cpf_dono, endereco, numero, bairro, cidade, cep):
        self.nome = nome
        self.cor = cor
        self.idade = idade
        self.raca = raca
        self.peso = peso
        self.dono = dono
        self.cpf_dono = cpf_dono
        self.endereco = endereco
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.cep = cep
        self.data_cadastro = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def __str__(self):
        return (f"Nome do Cachorro: {self.nome}\n"
                f"Cor: {self.cor}\n"
                f"Idade: {self.idade} anos\n"
                f"Raça: {self.raca}\n"
                f"Peso: {self.peso} kg\n"
                f"--- Dados do Dono ---\n"
                f"Nome do Dono: {self.dono}\n"
                f"CPF do Dono: {self.cpf_dono}\n"
                f"Endereço: {self.endereco}, {self.numero}\n"
                f"Bairro: {self.bairro}\n"
                f"Cidade: {self.cidade}\n"
                f"CEP: {self.cep}\n"
                f"Data do Cadastro: {self.data_cadastro}\n")
    def to_dict(self):
        return { 
            "nome" : self.nome, 
            "cor" : self.cor,
            "idade" : self.idade,
            "raca" : self.raca,
            "peso" : self.peso,
            "nome_dono" : self.dono,
            "cpf_dono" : self.cpf_dono,
            "endereco" : self.endereco,
            "bairro" : self.bairro,
            "cidade" : self.cidade,
            "cep" : self.cep,
            "data_cadastro" : self.data_cadastro
            }

    def salvar_cadastro(self,dados):
        os.makedirs("dados", exist_ok=True)
        dados.append(self.to_dict())
        nome_arquivo = "dados.json"
        with open(f"./dados/{nome_arquivo}", "w", encoding="utf-8") as f:
            json.dump(dados,f,ensure_ascii=True)
        print(f"Cadastro de {self.nome} salvo em {nome_arquivo}")