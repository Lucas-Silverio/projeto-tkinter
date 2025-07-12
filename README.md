# 📋 Projeto de Cadastro com Tkinter

Este é um projeto de interface gráfica desenvolvido com **Python** e **Tkinter**, utilizando **Orientação a Objetos (POO)**.
Adicionei conceitos de MVVM + clean architectures desenvolvidos por mim, enquanto aprendia sobre e aplicava no projeto.

Durante essa refatoração, aprendi e apliquei:

- ✅ Princípios do **MVVM**, separando logicamente as camadas de interface, lógica e dados
- ✅ Como estruturar um projeto com **Clean Architecture** (Domain(Model), Application(Use_case), Infrastructure(Repository), Interface(Views,ViewModels)
- ✅ Aplicação de boas práticas como **responsabilidade única**
- ✅ Validação de dados desacoplada da interface (ViewModel e UseCases)
- ✅ Organização do código para facilitar manutenção e expansão do projeto

## 🛠 Tecnologias Utilizadas

- **Python 3**
- **Tkinter** (interface gráfica)
- **JSON** (para armazenamento temporário dos dados)

## 🧠 Conceitos Aplicados

- Programação Orientada a Objetos (POO)
- Manipulação de arquivos JSON
- Componentes da interface Tkinter (Labels, Entry, Button, Toplevel, Treeview, etc.)
- Gerenciamento de eventos e interação com o usuário

## 🔍 Funcionalidades

- ✅ **Cadastro de registros** por meio de uma **tela modal**
- ✅ **Listagem** de registros em uma **Treeview**
- ✅ **Exclusão** de registros selecionados da lista
- ✅ Dados armazenados temporariamente em **arquivo JSON**
- ⏳ Planejamento futuro para salvar os dados em um **banco de dados PostgreSQL**

## 🚀 Como Executar

1. Certifique-se de ter o Python instalado (recomendado Python 3.8+)
2. Clone este repositório:
   ```bash
   git clone https://github.com/Lucas-Silverio/projeto-tkinter
   ```
3. Execute o projeto:
   ```bash
   principal.py
   ```
## 💡 Próximos Passos

- Integração com **banco de dados PostgreSQL**
✅ Funcionalidade de **edição** de registros existentes
- Validações mais robustas nos campos de entrada
- Aprimoramentos na interface e na experiência do usuário

## 👨‍🏫 Créditos

Este projeto foi desenvolvido como parte do curso do **SENAI**, com base em um código inicial fornecido pelo professor que havia somente um arquivo principal com uma classe de tela bem simples de cadastro salvando em txt.  
As funcionalidades adicionais, estrutura com orientação a objetos e melhorias na interface foram implementadas por mim como parte do aprendizado prático.
