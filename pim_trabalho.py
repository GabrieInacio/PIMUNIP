import hashlib
import json
import os

CAMINHO_USUARIOS = "usuarios.json"
CAMINHO_CURSOS = "cursos.json"

dados_usuarios = {}
dados_cursos = {}

def gerar_hash(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def carregar_dados_usuarios():
    global dados_usuarios
    if os.path.exists(CAMINHO_USUARIOS):
        with open(CAMINHO_USUARIOS, "r", encoding='utf-8') as arquivo:
            dados_usuarios = json.load(arquivo)
    else:
        dados_usuarios = {}

def salvar_dados_usuarios():
    with open(CAMINHO_USUARIOS, "w", encoding='utf-8') as arquivo:
        json.dump(dados_usuarios, arquivo, indent=4, ensure_ascii=False)

def carregar_dados_cursos():
    global dados_cursos
    if os.path.exists(CAMINHO_CURSOS):
        with open(CAMINHO_CURSOS, "r", encoding='utf-8') as arquivo:
            dados_cursos = json.load(arquivo)
    else:
        dados_cursos = {
            "Python Basico": ["Introdução", "Variáveis", "Estruturas de Controle"],
            "Pensamento Lógico Computacional": ["Conceitos Básicos", "Resolução de Problemas", "Algoritmos"],
            "Segurança Digital": ["Privacidade Online", "Proteção de Dados", "Boas Práticas de Segurança"]
        }
        salvar_dados_cursos()

def salvar_dados_cursos():
    with open(CAMINHO_CURSOS, "w", encoding='utf-8') as arquivo:
        json.dump(dados_cursos, arquivo, indent=4, ensure_ascii=False)

def exibir_menu_principal():
    carregar_dados_usuarios()
    carregar_dados_cursos()
    while True:
        print("\n========== PLATAFORMA DE EDUCAÇÃO DIGITAL SEGURA ==========")
        print("1. Fazer Login")
        print("2. Fazer Cadastro")
        print("3. Ver Cursos")
        print("4. Adicionar Módulos aos Cursos")
        print("5. Informações de Segurança")
        print("6. Sair")
        print("7. Remover Usuário")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            if realizar_login():
                exibir_menu_cursos()
        elif escolha == "2":
            realizar_cadastro()
        elif escolha == "3":
            listar_cursos()
        elif escolha == "4":
            adicionar_modulos()
        elif escolha == "5":
            exibir_info_seguranca()
        elif escolha == "6":
            print("Saindo...")
            break
        elif escolha == "7":
            remover_usuario()
        else:
            print("Opção inválida! Tente novamente.")

def exibir_menu_cursos():
    while True:
        print("\n--- Menu de Cursos ---")
        print("1. Ver Cursos Disponíveis")
        print("2. Cadastrar Módulos nos Cursos")
        print("3. Voltar ao Menu Principal")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            listar_cursos()
        elif escolha == "2":
            adicionar_modulos()
        elif escolha == "3":
            break
        else:
            print("Opção inválida! Tente novamente.")

def realizar_cadastro():
    print("\n--- Cadastro de Novo Usuário ---")
    nome_usuario = input("Nome de usuário: ")
    senha_usuario = gerar_hash(input("Senha: "))

    if nome_usuario in dados_usuarios:
        print("Usuário já cadastrado!")
    else:
        dados_usuarios[nome_usuario] = senha_usuario
        salvar_dados_usuarios()
        print("Cadastro realizado com sucesso!")

def realizar_login():
    print("\n--- Login ---")
    nome_usuario = input("Nome de usuário: ")
    senha_usuario = gerar_hash(input("Senha: "))

    if nome_usuario in dados_usuarios and dados_usuarios[nome_usuario] == senha_usuario:
        print("Login realizado com sucesso!")
        return True
    else:
        print("Usuário ou senha incorretos!")
        return False

def listar_cursos():
    print("\n--- Cursos Disponíveis ---")
    if not dados_cursos:
        print("Nenhum curso disponível no momento.")
    for nome_curso, lista_modulos in dados_cursos.items():
        print(f"\nCurso: {nome_curso}")
        print("Módulos:")
        for modulo in lista_modulos:
            print(f"  - {modulo}")

def adicionar_modulos():
    print("\n--- Adicionar Módulos aos Cursos ---")
    nome_curso = input("Digite o nome do curso: ")
    if nome_curso in dados_cursos:
        nome_modulo = input("Digite o nome do módulo: ")
        dados_cursos[nome_curso].append(nome_modulo)
        salvar_dados_cursos()
        print(f"Módulo '{nome_modulo}' adicionado ao curso '{nome_curso}'.")
    else:
        criar_curso = input("Curso não encontrado. Deseja criar este curso? (s/n): ").lower()
        if criar_curso == "s":
            nome_modulo = input("Digite o nome do módulo inicial: ")
            dados_cursos[nome_curso] = [nome_modulo]
            salvar_dados_cursos()
            print(f"Curso '{nome_curso}' criado com o módulo '{nome_modulo}'.")

def remover_usuario():
    print("\n--- Remover Usuário ---")
    nome_usuario = input("Digite o nome do usuário que deseja remover: ")

    if nome_usuario in dados_usuarios:
        confirmar = input(f"Tem certeza que deseja remover o usuário '{nome_usuario}'? (s/n): ").lower()
        if confirmar == "s":
            del dados_usuarios[nome_usuario]
            salvar_dados_usuarios()
            print(f"Usuário '{nome_usuario}' removido com sucesso!")
        else:
            print("Remoção cancelada.")
    else:
        print("Usuário não encontrado.")

def exibir_info_seguranca():
    print("\n--- Informações de Segurança ---")
    print("Dicas de Segurança:")
    print("- Use senhas fortes e únicas.")
    print("- Nunca compartilhe sua senha com terceiros.")
    print("- Habilite autenticação em dois fatores quando possível.")
    print("- Mantenha seu software sempre atualizado.")

if __name__ == "__main__":
    exibir_menu_principal()
