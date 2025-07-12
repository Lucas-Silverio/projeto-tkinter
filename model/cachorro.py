import datetime
import re

class Cachorro:
    def __init__(self,nome, cor, idade, raca, peso, dono, cpf_dono, endereco, numero, bairro, cidade, cep,id = 0):
        self.validar_dados(nome, cor, idade, raca, peso, dono, cpf_dono, endereco, numero, bairro, cidade, cep,id)
        self.id = id
        self.nome = nome
        self.cor = cor
        self.idade = int(idade)
        self.raca = raca
        self.peso = float(peso)
        self.dono = dono
        self.cpf_dono = cpf_dono
        self.endereco = endereco
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.cep = cep
        self.data_cadastro = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def validar_dados(self,*args):
        campos = ['nome','cor','idade','raca','peso','dono','cpf_dono','endereco','numero','bairro','cidade','cep','id']
        for i,x in zip(args,campos):
            if x == "idade":
                try:
                    i = int(i)
                except ValueError as e :
                    raise ValueError("O campo Idade deve ser inteiro.")
                if i < 0:
                    raise ValueError("O campo Idade não pode ser negativo.")
            elif x == "peso":
                try:
                    i = float(i)
                except ValueError as e:
                    raise ValueError("O campo Peso deve ser decimal.")
            if x != "idade" and x != "peso" and x != "id":
                if i.strip() == "":
                    raise ValueError("Preencha todos os campos.")
                if i != i.strip():
                    raise ValueError("Os campos não podem iniciar ou terminar com espaço.")
                if re.search(r"\s{2,}", i):
                    raise ValueError("Os campos não podem conter múltiplos espaços seguidos.")
            if x == "cpf_dono":
                valido = self.validar_campo_cpf(i)
                if not valido:
                    raise ValueError("O campo CPF do Dono deve manter o formato: XXX.XXX.XXX-XX")

    def validar_campo_cpf(self,cpf):
        if len(cpf) == 14:
            formato_valido = [False,False,False,False,False]
            if "".join(cpf[:3]).isdigit():
                formato_valido[0] = True
            if "".join(cpf[4:7]).isdigit():
                formato_valido[1] = True
            if "".join(cpf[8:11]).isdigit():
                formato_valido[2] = True
            if "".join(cpf[-2:]).isdigit():
                formato_valido[3] = True
            pontos_eh_hifen = [item for i, item in enumerate(cpf) if i in (3,7,11)]
            if pontos_eh_hifen[0] == "." and pontos_eh_hifen[1] == "." and pontos_eh_hifen[2] == "-":
                formato_valido[4] = True
            for i in formato_valido:
                if not i:
                    return False
            return True
        else:
            return False
        
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
            "id": self.id,
            "nome" : self.nome, 
            "cor" : self.cor,
            "idade" : self.idade,
            "raca" : self.raca,
            "peso" : self.peso,
            "nome_dono" : self.dono,
            "cpf_dono" : self.cpf_dono,
            "endereco" : self.endereco,
            "numero" : self.numero,
            "bairro" : self.bairro,
            "cidade" : self.cidade,
            "cep" : self.cep,
            "data_cadastro" : self.data_cadastro
            }