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
            try:
                dados_usuarios = json.load(arquivo)
            except (json.JSONDecodeError, ValueError):
                dados_usuarios = {}
    else:
        dados_usuarios = {}

def salvar_dados_usuarios():
    with open(CAMINHO_USUARIOS, "w", encoding='utf-8') as arquivo:
        json.dump(dados_usuarios, arquivo, indent=4, ensure_ascii=False)

def carregar_dados_cursos():
    global dados_cursos
    if os.path.exists(CAMINHO_CURSOS):
        with open(CAMINHO_CURSOS, "r", encoding='utf-8') as arquivo:
            try:
                dados_cursos = json.load(arquivo)
            except (json.JSONDecodeError, ValueError):
                dados_cursos = {}
    if not dados_cursos:
        dados_cursos.update({
            "Python Básico": {
                "Introdução": "Este módulo apresenta o que é Python e suas aplicações.",
                "Variáveis": "Aprenda o que são variáveis, tipos de dados e como usá-las.",
                "Estruturas de Controle": "Conheça estruturas como if, for e while."
            },
            "Pensamento Lógico Computacional": {
                "Conceitos Básicos": "Entenda como pensar logicamente para resolver problemas.",
                "Resolução de Problemas": "Aprenda técnicas para dividir e resolver problemas complexos.",
                "Algoritmos": "Descubra como criar algoritmos eficientes para suas soluções."
            },
            "Segurança Digital": {
                "Privacidade Online": "Como manter sua privacidade e dados protegidos na internet.",
                "Proteção de Dados": "Entenda como proteger informações sensíveis.",
                "Boas Práticas de Segurança": "Veja dicas e hábitos para navegar com segurança."
            }
        })
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
        print("3. Informações de Segurança")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            if realizar_login():
                exibir_menu_cursos()
        elif escolha == "2":
            realizar_cadastro()
        elif escolha == "3":
            exibir_info_seguranca()
        elif escolha == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

def exibir_menu_cursos():
    while True:
        print("\n--- Menu de Cursos ---")
        print("1. Ver Cursos Disponíveis")
        print("2. Voltar ao Menu Principal")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            listar_cursos()
        elif escolha == "2":
            break
        else:
            print("Opção inválida! Tente novamente.")

def realizar_cadastro():
    print("\n--- Cadastro de Novo Usuário ---")
    nome_usuario = input("Nome completo: ")
    email_usuario = input("Email: ")

    if any(usuario.get("email") == email_usuario for usuario in dados_usuarios.values()):
        print("Email já cadastrado!")
        return

    senha_usuario = gerar_hash(input("Senha: "))

    dados_usuarios[nome_usuario] = {
        "senha": senha_usuario,
        "email": email_usuario
    }

    salvar_dados_usuarios()
    print("Cadastro realizado com sucesso!")

def realizar_login():
    print("\n--- Login ---")
    email_digitado = input("Email: ")
    senha_digitada = gerar_hash(input("Senha: "))

    for usuario in dados_usuarios.values():
        if usuario["email"] == email_digitado and usuario["senha"] == senha_digitada:
            print("Login realizado com sucesso!")
            return True

    print("Email ou senha incorretos!")
    return False

def listar_cursos():
    print("\n--- Cursos Disponíveis ---")
    if not dados_cursos:
        print("Nenhum curso disponível no momento.")
        return

    cursos_lista = list(dados_cursos.keys())
    for i, nome_curso in enumerate(cursos_lista, start=1):
        print(f"{i}. {nome_curso}")

    try:
        escolha = int(input("Selecione um curso pelo número (ou 0 para voltar): "))
        if escolha == 0:
            return
        curso_escolhido = cursos_lista[escolha - 1]
    except (ValueError, IndexError):
        print("Opção inválida!")
        return

    print(f"\nCurso selecionado: {curso_escolhido}")
    print("Módulos:")
    modulos = list(dados_cursos[curso_escolhido].keys())
    for i, modulo in enumerate(modulos, start=1):
        print(f"{i}. {modulo}")

    try:
        escolha_modulo = int(input("Selecione um módulo pelo número (ou 0 para voltar): "))
        if escolha_modulo == 0:
            return
        modulo_escolhido = modulos[escolha_modulo - 1]
        print(f"\nConteúdo do módulo '{modulo_escolhido}':")
        print(dados_cursos[curso_escolhido][modulo_escolhido])
    except (ValueError, IndexError):
        print("Opção de módulo inválida!")


def exibir_conteudo_modulo():
    curso = input("Digite o nome do curso: ")
    if curso not in dados_cursos:
        print("Curso não encontrado.")
        return
    modulo = input("Digite o nome do módulo: ")
    if modulo in dados_cursos[curso]:
        print(f"\nConteúdo do módulo '{modulo}':")
        print(dados_cursos[curso][modulo])
    else:
        print("Módulo não encontrado nesse curso.")

def exibir_info_seguranca():
    print("\n--- Informações de Segurança ---")
    print("Dicas de Segurança:")
    print("- Use senhas fortes e únicas.")
    print("- Nunca compartilhe sua senha com terceiros.")
    print("- Habilite autenticação em dois fatores quando possível.")
    print("- Mantenha seu software sempre atualizado.")

if __name__ == "__main__":
    exibir_menu_principal()
