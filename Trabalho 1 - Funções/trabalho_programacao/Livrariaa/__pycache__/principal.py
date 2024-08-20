# principal.py

from funcoes import adicionar_livro, mostrar_tabela, mostrar_livro, remover_livro, mostrar_menu

def executar_programa():
    """
    Gerencia o fluxo principal do programa com base na escolha do usuário.
    """
    livros = []

    while True:
        escolha = mostrar_menu()
        print()  # Espaçamento

        if escolha == 1:
            # Adicionar livro
            livros = adicionar_livro(livros)
        
        elif escolha == 2:
            # Mostrar tabela de livros
            mostrar_tabela(livros)
        
        elif escolha == 3:
            # Ver detalhes de um livro
            mostrar_livro(livros)
        
        elif escolha == 4:
            # Remover livro
            remover_livro(livros)
        
        elif escolha == 5:
            # Sair
            print("Saindo do programa.")
            break
        
        else:
            print("Opção inválida, por favor escolha novamente.")
            print()  # Espaçamento

if __name__ == "__main__":
    executar_programa()
