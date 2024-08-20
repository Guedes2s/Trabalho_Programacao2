# funcoes.py

def adicionar_livro(livros):
    """
    Adiciona um livro ao dicionário de livros.

    Args:
        livros (list): Lista contendo os livros cadastrados.

    Returns:
        list: Lista atualizada com o novo livro.
    """
    nome_livro = input("Digite o nome do livro: ")
    autor = input("Digite o nome do autor: ")
    ano_publicacao = input("Digite o ano de publicação (formato AAAA): ")
    
    livros.append({
        'nome_livro': nome_livro,
        'autor': autor,
        'ano_publicacao': ano_publicacao
    })
    
    print("\nLivro adicionado com sucesso.")
    return livros

def mostrar_tabela(livros):
    """
    Exibe uma tabela com todos os livros cadastrados.

    Args:
        livros (list): Lista contendo os livros cadastrados.
    """
    print("\nTabela de Livros Cadastrados")
    print(f"{'Nome do Livro':<30} {'Autor':<30} {'Ano de Publicação':<15}")
    print("-" * 75)
    
    if not livros:
        print("Nenhum livro cadastrado.")
    else:
        for livro in livros:
            print(f"{livro['nome_livro']:<30} {livro['autor']:<30} {livro['ano_publicacao']:<15}")

def mostrar_livro(livros):
    """
    Exibe detalhes de um livro específico.

    Args:
        livros (list): Lista contendo os livros cadastrados.
    """
    nome_livro = input("Digite o nome do livro para visualizar os detalhes: ")
    print()  # Espaçamento
    
    for livro in livros:
        if livro['nome_livro'].lower() == nome_livro.lower():
            print(f"Nome do Livro: {livro['nome_livro']}")
            print(f"Autor: {livro['autor']}")
            print(f"Ano de Publicação: {livro['ano_publicacao']}")
            print()  # Espaçamento
            return
    
    print("Livro não encontrado.")
    print()  # Espaçamento

def remover_livro(livros):
    """
    Remove um livro da lista de livros.

    Args:
        livros (list): Lista contendo os livros cadastrados.

    Returns:
        list: Lista atualizada sem o livro removido.
    """
    nome_livro = input("Digite o nome do livro a ser removido: ")
    print()  # Espaçamento
    
    for livro in livros:
        if livro['nome_livro'].lower() == nome_livro.lower():
            livros.remove(livro)
            print("Livro removido com sucesso.")
            print()  # Espaçamento
            return
    
    print("Livro não encontrado.")
    print()  # Espaçamento

def mostrar_menu():
    """
    Exibe o menu principal e coleta a escolha do usuário.

    Returns:
        int: Escolha do usuário.
    """
    print("\nMenu:")
    print("1. Adicionar livro")
    print("2. Mostrar tabela de livros")
    print("3. Ver detalhes de um livro")
    print("4. Remover um livro")
    print("5. Sair")
    escolha = int(input("Escolha uma opção: "))
    return escolha

def mostrar_sobre():
    """
    Exibe informações sobre o programa.
    """
    print("\nSobre o Programa")
    print("Este é um sistema para gerenciar uma livraria.")
    print("Você pode adicionar livros, ver uma tabela com todos os livros cadastrados, ver detalhes de um livro, remover livros e sair do programa.")
    print("Desenvolvido por: [Seu Nome]")
    print()  # Espaçamento
