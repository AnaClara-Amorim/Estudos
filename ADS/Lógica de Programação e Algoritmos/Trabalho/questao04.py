# Você e sua equipe de programadores foram contratados por pequena empresa para desenvolver o software de gerenciamento de livros. Este software deve ter o seguinte menu e opções: 
#1)Cadastrar Livro 2)Consultar Livro 1.Consultar Todos  2.Consultar por Id 3.Consultar por Autor 4.Retornar ao menu 3)Remover Livro 4)Encerrar Programa

# Lista para amarzenar os livros
lista_livro = []
# Variável global para controlar os IDS
id_global = 0

# Função para cadastrar um livro
def cadastrar_livro(id):
    # Imputs para cadastro de livro
    nome = input("Por favor, entre com o nome do livro: ")
    autor = input("Por favor, entre com o autor do livro: ")
    editora = input("Por favor, entre com a editora do livro: ")

    # Dicionário 
    livro = {'id': id, 'nome': nome, 'autor': autor, 'editora': editora}

    # Copiando o dicionário para dentro da função lista_livro()
    lista_livro.append(livro)
    print("Livro cadastrado com sucesso!\n")

# Função para consultar um livro
def consultar_livro():     
     while True: # Laço de repetição 
        # Menu de consulta de livros
        print("""MENU DE CONSULTA DE LIVROS
                 1 - Consultar todos os livros
                 2 - Consultar livro por id
                 3 - Consultar livro(s) por autor
                 4 - Retornar ao menu principal """)
     
        # Entrada do modo de consulta
        opcao = int(input("Escolha uma opção: "))
     
        # Aninhamento de ifs    

        if (opcao == 1): # Consulta de todos livros e seus dados
            if lista_livro:
                for livro in lista_livro: # Laço para leitura de dados registrados em livros dentro de lista_livros
                    print(f"ID: {livro['id']}, Nome: {livro['nome']}, Autor: {livro['autor']}, Editora: {livro['editora']}")
                else:
                    print("Nenhum livro cadastrado.")    
        elif (opcao == 2): # Consulta por id com dados do livro
            id_consulta = int(input("Digite o ID do livro: ")) # Input pra consulta de livro por ID
            livro_encontrado = False # Status atual do livro antes da procura
            for livro in lista_livro: # Laço para pesquisa do livro dentro de lista_livros
                if livro['id'] == id_consulta: # Checagem de id
                    print(f"ID: {livro['id']}, Nome: {livro['nome']}, Autor: {livro['autor']}, Editora: {livro['editora']}")
                    livro_encontrado = True
                    break 
                if not livro_encontrado:
                    print("Livro não encontrado.")              
        elif (opcao == 3): # Consulta por autor e livros cadastrados em sua autoria
            autor_consulta = input("Digite o nome do autor pra consulta: ") # Input pra consulta de livro por autos
            livros_encontrados = [livro for livro in lista_livro if livro['autor'] == autor_consulta] # Checagem de autor 
            if livros_encontrados: # Exibição dos livros no nome do autor
                for livro in livros_encontrados:
                    print(f"ID: {livro['id']}, Nome: {livro['nome']}, Autor: {livro['autor']}, Editora: {livro['editora']}")            
        elif(opcao == 4): # Retorno ao menu principal
             break
        else: # Se a digitação for errada
            print("Opção inválida. Tente novamente.")

# Função para remoção de um livro por id
def remover_livro():
    # Laço de repetição
    while True:
        id_remover = int(input("Digite o ID do livro a ser removido: "))
        for livro in lista_livro:
            if livro['id'] == id_remover: # Checagem de id para remoção
                lista_livro.remove(livro) # Função para remoção do livro selecionado
                print("Livro removido com sucesso")
                return
        print("ID inválido. Tente novamente.")

# MENU PRINCIPAL
def main(): # Função main
    global id_global # Definida no escopo global 
    while True: # Laço de repetição
        # Começo do menu principal
        print("Bem-vindo à Livraria da Ana Clara")
        print("---------------------------------")
        print("---------- MENU PRINCIPAL -------")
        print("Escolha a opção desejada:")
        print("""
            1 - Cadastrar livro
            2 - Consultar livro
            3 - Remover livro
            4 - Encerrar programa
                """)
        
        opcao = input("Escolha uma opção: ") # Input da escolha
            
        if opcao == "1":
            id_global += 1 # Garante que toda vez que chamado, a id_global receba ela mesma mais 1
            cadastrar_livro(id_global) # Chamando a função de cadastrar livro e passando a id_gloval
        elif opcao == "2":
            consultar_livro() # Chamando a função de consultar livro
        elif opcao == "3":
            remover_livro() # Chamando a função de remoção de livro
        elif opcao == "4":
            print("Encerrando o programa. Até mais!") # Encerrando o programa
            break
        else:
            print("Opção inválida. Tente novamente.") # Caso não seja digitado de 1 a 4

# Ponto de entrada do programa e chamado da função main
if __name__ == "__main__":
    main()