
# funcoes.py

def adicionar_livro(livros):
    
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
    
    print("\nTabela de Livros Cadastrados")
    print(f"{'Nome do Livro':<30} {'Autor':<30} {'Ano de Publicação':<15}")
    print("-" * 75)
    
    if not livros:
        print("Nenhum livro cadastrado.")
    else:
        for livro in livros:
            print(f"{livro['nome_livro']:<30} {livro['autor']:<30} {livro['ano_publicacao']:<15}")

def mostrar_livro(livros):
    
    nome_livro = input("Digite o nome do livro para visualizar os detalhes: ")
    print()
    
    for livro in livros:
        if livro['nome_livro'].lower() == nome_livro.lower():
            print(f"Nome do Livro: {livro['nome_livro']}")
            print(f"Autor: {livro['autor']}")
            print(f"Ano de Publicação: {livro['ano_publicacao']}")
            print()
            return
    
    print("Livro não encontrado.")
    print() 

def remover_livro(livros):
    
    nome_livro = input("Digite o nome do livro a ser removido: ")
    print() 
    
    for livro in livros:
        if livro['nome_livro'].lower() == nome_livro.lower():
            livros.remove(livro)
            print("Livro removido com sucesso.")
            print() 
            return
    
    print("Livro não encontrado.")
    print() 

def mostrar_menu():
    
    print("\nMenu:")
    print("1. Adicionar livro")
    print("2. Mostrar tabela de livros")
    print("3. Ver detalhes de um livro")
    print("4. Remover um livro")
    print("5. Sair")
    escolha = int(input("Escolha uma opção: "))
    return escolha


