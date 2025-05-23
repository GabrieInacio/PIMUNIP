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
{
  "Python Básico": {
    "Introdução": "\nPython é uma linguagem de programação de alto nível, criada por Guido van Rossum e lançada em 1991. Sua filosofia preza pela legibilidade e simplicidade, tornando-se ideal para iniciantes e profissionais experientes. Python é multiparadigma, suportando programação procedural, orientada a objetos e funcional. Sua vasta comunidade e biblioteca padrão robusta facilitam o desenvolvimento de aplicações web, análise de dados, automação, inteligência artificial, entre outros.\n\nVantagens:\n- Sintaxe simples e clara.\n- Grande quantidade de bibliotecas e frameworks.\n- Comunidade ativa e colaborativa.\n\nInstalação:\n- Download em python.org.\n- IDEs recomendadas: VSCode, PyCharm, Jupyter Notebook.\n\nPrimeiro programa em Python:\nprint(\"Olá, mundo!\")\n\nEsse comando imprime uma mensagem na tela, demonstrando a simplicidade da linguagem.\n",
    "Variáveis": "\nVariáveis são espaços de memória utilizados para armazenar dados que podem ser manipulados durante a execução do programa. Em Python, não é necessário declarar o tipo da variável, pois a linguagem é dinamicamente tipada.\n\nExemplo:\nnome = \"Ana\"\nidade = 25\naltura = 1.70\n\nTipos de dados comuns:\n- int: números inteiros.\n- float: números decimais.\n- str: cadeias de caracteres.\n- bool: valores booleanos (True/False).\n\nConversão de tipos:\nidade = \"25\"\nidade = int(idade)\n\nBoas práticas:\n- Nomes de variáveis devem ser descritivos.\n- Utilizar letras minúsculas e underscore (_).\n",
    "Estruturas de Controle": "\nEstruturas de controle definem o fluxo de execução do programa.\n\nCondicional if:\nidade = 18\nif idade >= 18:\n    print(\"Maior de idade\")\nelse:\n    print(\"Menor de idade\")\n\nLaço for:\nfor i in range(5):\n    print(i)\n\nLaço while:\ncontador = 0\nwhile contador < 5:\n    print(contador)\n    contador += 1\n\nImportância:\n- Automatizam tarefas repetitivas.\n- Tomam decisões baseadas em condições.\n"
  },
  "Pensamento Lógico Computacional": {
    "Conceitos Básicos": "\nO pensamento lógico computacional é a habilidade de resolver problemas de forma estruturada, utilizando princípios da lógica matemática e da computação.\n\nPrincipais conceitos:\n- Sequência: executar comandos em ordem.\n- Decisão: escolher caminhos baseados em condições.\n- Repetição: executar ações múltiplas vezes.\n\nHabilidades desenvolvidas:\n- Análise crítica.\n- Organização do raciocínio.\n- Modelagem de soluções.\n\nExemplo: preparar um café envolve uma sequência lógica — ferver água, adicionar café, misturar.\n",
    "Resolução de Problemas": "\nResolver problemas computacionais envolve:\n1. Compreensão: analisar o problema.\n2. Planejamento: elaborar a solução.\n3. Implementação: programar a solução.\n4. Teste: verificar se o resultado está correto.\n\nEstratégias:\n- Dividir o problema em partes menores.\n- Buscar padrões.\n- Utilizar abstração.\n\nExemplo prático:\nProblema: calcular a média de três números.\nSolução:\na = 5\nb = 7\nc = 9\nmedia = (a + b + c) / 3\nprint(media)\n",
    "Algoritmos": "\nAlgoritmo é um conjunto finito de passos bem definidos para resolver um problema.\n\nCaracterísticas:\n- Clareza.\n- Finitude.\n- Eficácia.\n\nExemplo de algoritmo para verificar se um número é par ou ímpar:\n1. Receber um número.\n2. Dividir o número por 2.\n3. Se o resto for 0, é par; senão, ímpar.\n\nImplementação:\nnum = int(input(\"Digite um número: \"))\nif num % 2 == 0:\n    print(\"Par\")\nelse:\n    print(\"Ímpar\")\n\nFluxogramas são úteis para representar algoritmos visualmente.\n"
  },
  "Segurança Digital": {
    "Privacidade Online": "\nPrivacidade online refere-se à proteção de dados pessoais na internet, impedindo acesso não autorizado.\n\nRiscos:\n- Roubo de identidade.\n- Vazamento de informações.\n- Monitoramento indevido.\n\nBoas práticas:\n- Utilizar senhas fortes.\n- Não compartilhar dados pessoais indiscriminadamente.\n- Configurar corretamente as opções de privacidade em redes sociais.\n\nFerramentas recomendadas:\n- VPNs (Redes Privadas Virtuais).\n- Autenticação em dois fatores (2FA).\n",
    "Proteção de Dados": "\nRefere-se ao conjunto de medidas para garantir a integridade e segurança das informações pessoais e corporativas.\n\nPrincípios:\n- Confidencialidade: dados acessados apenas por pessoas autorizadas.\n- Integridade: dados não podem ser alterados sem permissão.\n- Disponibilidade: dados disponíveis sempre que necessário.\n\nMedidas de proteção:\n- Criptografia.\n- Backups regulares.\n- Antivírus e firewalls atualizados.\n\nLegislação:\n- Lei Geral de Proteção de Dados (LGPD) no Brasil.\n- GDPR na União Europeia.\n",
    "Boas Práticas de Segurança": "\nSão ações cotidianas que minimizam riscos de incidentes digitais.\n\nDicas importantes:\n- Atualizar sistemas e aplicativos regularmente.\n- Desconfiar de e-mails e links suspeitos (phishing).\n- Utilizar senhas únicas para cada serviço.\n- Ativar a autenticação de dois fatores sempre que possível.\n- Fazer backups frequentes.\n\nAlém disso, a educação em segurança é essencial: conhecer as ameaças e saber como se proteger.\n"
  }
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
