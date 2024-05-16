# Escreva um algoritmo que permita cadastrar jogos, informando nome e a qual console ele pertence. Para isso, criar um menu de opções contendo: cadastrar novo item, listar tudo o que foi cadastrado e sair. Um item pra cada menu. Armazenar os dados em um arquivo de texto.

def valida_int(pergunta, min, max):
    try:
        x = int(input(pergunta))
        
        while ((x < min) or (x > max)):
            x = int(input(pergunta))
        return x
    except ValueError:
            print("Erro: Entrada inválida. Por favor, insira um número de 1 a 3.")

def existeArquivo (nomeArquivo):
    try:
        #Usando função open, close, read, write
        a = open(nomeArquivo, 'r+')  #ANTES ERA RT
        a.close()    
    except FileNotFoundError:
        return False
    else: True

def criarArquivo (nomeArquivo):
    try:
        #Usando função open, close, read, write
        a = open(nomeArquivo, 'wt+') 
        a.close()    
    except:
        print("Erro na criação do arquivo")
    else: 
        print(f"Arquivo {nomeArquivo} criado com sucesso! \n")

def cadastrarJogo (nomeArquivo, nomeJogo, nomeVideogame):
    try: 
        a = open(nomeArquivo, 'a') #Antes de eu modificar era at
    
    except:
        print('Erro ao abrir o arquivo.')
        
    else: 
        a.write(f"Nome do jogo: {nomeJogo} | Nome do console: {nomeVideogame} \n")
    
    finally:
        a.close()
    
def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt') #Antes de eu modificar era rt
    except:
        print("Erro ao ler o arquivo.")
    else:
        print(a.read())
    finally:
        a.close()

# Programa principal 

arquivo = 'games.txt'
if existeArquivo(arquivo):
    print("Arquivo localizado no computador")
else:
    print("Arquivo inexistente")
    criarArquivo(arquivo)

while True:
    print ('Menu')
    print ('1 - Cadastrar novo item.')
    print ('2 - Listar cadastros.')
    print ('3 - Sair.')

    #Validação da opção do menu, apenas 1, 2 ou 3

    op = valida_int("Escolha a opção desejada: ", 1, 3)

    if (op == 1): # Novo item
        print("Opção de cadastrar novo item selecionada... \n")
        nomeJogo = input("Nome do jogo: ")
        nomeVideogame = input("Nome do console: ")

        cadastrarJogo(arquivo, nomeJogo, nomeVideogame)


    elif (op == 2): # Listar
        print("Opção de listar novo item selecionada... \n")

        listarArquivo(arquivo)

    elif (op == 3):
        print ("Encerrando o programa")
        break


