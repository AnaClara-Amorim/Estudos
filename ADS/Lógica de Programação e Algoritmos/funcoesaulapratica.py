# Interactive Help

#help(print)

# Docstrings, strings inseridas dentro do código do python que explicam o funcionamento dele

def soma (x = 0, y = 0, z = 0):
    """Retorna o somatório de 3 valores"""
    return x + y + z

print (soma(1, 2, 3))
help (soma)

#Função que calcule fatorial de numero, e retorne o sei valor. Fazer validação de dados por meio de outra função, permitindo apenas valores positivo. Criar help da função.

def fatorial (num):

    """
    Função que calcula o fatorial de um número de um número inteiro

    """

    fat = 1 
    if num == 0:
        return fat #pois fatorial de zero é um
    # Esta parte só executa caso num > 0
    for i in range (1, num + 1, 1):
        fat *= i
    
    return fat

def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x





#x = int(input("Digite um valor para calcular o fatorial: "))

x = valida_int("Digite um valor para calcular o fatorial: ", 0, 9999999)

print(f'{x}! = {fatorial(x)}')
    
help(fatorial)


    

