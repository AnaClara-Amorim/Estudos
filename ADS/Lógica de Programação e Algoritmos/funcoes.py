# Criando função  |  def nome-da-funcao ():
def realce ():
    print('|', '_' * 10, '|')
    print('|', '_' * 10, '|')
    print('     MENU      ')
    print('|', '_' * 10, '|')
    print('|', '_' * 10, '|')

# Chamando a funcao
realce()

# Passagem de parâmetros (dados recebidos pelas funções) em uma função | def nome-da-função (variável):

def barras (s1):
    print('|', '_' * 10, '|')
    print('|', '_' * 10, '|')
    print(s1)
    print('|', '_' * 10, '|')
    print('|', '_' * 10, '|')

barras('     MENU      ')
barras('  BATATINHAS   ')

# É possível passar mais de um parâmetro

def sub2 (x, y):
    res = x - y
    print(res)

sub2(10, 3)
sub2(y = 10, x = 30)

# Os parâmetros podem ser definidos ou não 

def soma1 (x = 0, y = 0, z = 0):
    resp = x + y + z
    print (resp)

soma1 (1, 2, 3)
soma1 (1,2)
soma1(1)
soma1()

# Exercício
# Escrever uma rotina que crie uma borda ao redor de uma palavra. A rotina deve receber como parâmetro a palavra a ser destacada. O tamanho da caixa de texto deverá ser adaptável, de acordo com o tamanho da palavra. 

def borda (s1):
    tam = len(s1)
    # Só faz se existir algum caractere
    if tam:
        print ('+', '-' * tam, '+')
        print ('|', s1, '|')
        print ('+', '-' * tam, '+')

borda("Olá, mundo!")
borda ("Ana Clara")

# Escopo de variáveis, determina onde uma variável pode ser utilizada 
# Pode ser local ou global
# Local: Variáveis criadas dentro de uma função, por exemplo    
# Global: Criadas dentro do programa principal

#def omelete():
#    ovos = 12 # Variável local

#omelete()
#print(ovos) Dá erro

#def omelete():
    #print(ovos)

#ovos = 12 variável local
#omelete()

# Instrução global, força o programa a não criar uma variável local de mesmo nome e manipoular somente a global dentro de uma função

#def omelete():
 #   global ovos
  #  ovos = 6

#ovos = 12
#omelete()
#print (ovos)

# Retorno de valores em funções

# Procedimento: Rotina sem retorno | Função: Rotina com retorno

def soma3 (x = 0, y = 0, z = 0):
    res = x + y + z
    return res

retornado = soma3 (10, 12, 12)
print (retornado)

retornado1 = soma3(1, 2, 3) # Atribui à variável o valor a ser jogado na função
retornado2 = soma3(1,2)
retornado3 = soma3 ()
print (f'Somatórios: {retornado1}, {retornado2}, e {retornado3}.') # Mostra o resultado

# Escreva uma função para validar uma string. Essa função recebe como parâmetro a string, o número mínimo e máximo de caracteres. Retorne verdadeiro se o tamanho da string estiver entre os valores de min e max, e falso caso contrário. 

def valida_string (pergunta, min, max):
    s1 = input(pergunta)
    tam = len(s1)
    while ((tam < min) or (tam > max)):
        s1 = input(pergunta)
        tam = len(s1)
        return s1

x = valida_string("Digite uma string: ", 10, 30)
print('Você digitou a string: {} \n Dado válido. Encerrando o programa...'.format(x))

# Recursos para tratar erros, como ZeroDivisionError ou ValueError

i = 0 

while True:
    try:
        x = int(input("Por favor, digite um NÚMERO: "))
        break
    except ValueError:
        print("Oops, parece que você digitou um número errado, tente novamente")


o = 0
while True:
    try:
        nome = input("Por favor, digite o seu nome: ")
        ind = int(input("Digite um índice do seu nome: "))
        print (nome[ind])
        break
    except ValueError:
        print("Nome inválido. Tente novamente!")
    except IndexError:
        print("Índice inválido. Tente novamente!")
    finally:
        print:(f"Tentativa {o}")
        o += 1


# Função lambda

res = lambda x: x * x
print (res(3))

soma = lambda x, y: x + y
print(soma(3,5))

# Faça uma função lambda que recebe dois valroes numéricos como parâmetro. Ao primeiro valor, sempre some 5. Em seguida, multiplique ambos e retorne o resultado. 

calc = lambda a, b: (a + 5) * b
print(calc(5, 10))