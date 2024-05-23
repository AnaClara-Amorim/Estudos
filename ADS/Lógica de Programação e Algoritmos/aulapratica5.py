#Importando Bibliotecas, Tuplas, listas, dicionários e strings.

# Importando bibliotecas

#Python.org > Doc > Library References 
# import math sem abreviação 
import math as m # Importando com abreviação
# Para não pesar, podemos puxar somente a função desejada
from math import sqrt 
print(m.sqrt(9)) # Nome da biblioteca.função

# Dada uma LISTA contendo as notas de alunos em uma disciplina, escreva uma expressão para: notas = [9, 7, 7, 10, 3, 9, 6, 6, 2] a) encontrar quantos alunos tiraram nota 7 b) alterar a última nota para 4

notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]
print(notas)
print(f'Existem {notas.count(7)} notas 7')
notas[-1] = 4
print(notas)
# Encontrar maior nota
print(max(notas))
# Encontar menor nota
print(min(notas))
# Ordenar lista
notas.sort()
print (notas)
# Soma de todos
print(sum(notas) / len(notas))

# Escreva um algoritmo que crie uma tupla com 5 palavras. Encontre dentro dessa tupla as vogais de cada palavra. Faça um print na tela com o nome da palavra e suas respectivas vogais. 

palavras = ("Mario", "Luigi", "Peach", "Yoshi", "Bowser")

for palavra in palavras:
    print(f'\n Palavra: {palavra.upper()}. Vogais: ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')

# Crie um jogo de pedra papel ou tesoura. Você deverá jogar contra o computador. Você irá sempre escolher uma das opções: 1 - pedra, 2 - papel, 3 - tesoura. O computador irá sempre sortear um número de 1 até 3 para jgoar. Armazene todos os resultados em uma lista e, no final, apresente o vencedor. Encerre o programa ao digitar zero. 


#Função de validação
import random
def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def vencedor(jogador1, jogador2):
    global v1, v2, empate # puxa as variáveis globais
    if jogador1 == 1: # Pedra
        if jogador2 == 1: # Pedra
            empate +=1
        elif jogador2 == 2: # Papel
            v2 += 1
        elif jogador2 == 3: # Tesoura
            v1 += 1 
    elif jogador1 == 2: # Papel
        if jogador2 == 2:
            empate +=1
        elif jogador2 == 2: # Papel
            empate += 1
        elif jogador2 == 3: # Tesoura
            v2 += 1
    elif jogador1 == 3: # Tesoura
        if jogador2 == 3: # Tesoura
            empate +=1
        elif jogador2 == 1: # Pedra
            v2= 1
        elif jogador2 == 2: # Papel
            v1 += 1
    
    resultados = [v1, v2, empate]
    return resultados


print("\n JOKENPO")
print ('1 - Pedra \n2 - Papel \n3 - Tesoura \n0 - Para terminar o jogo')

jogadas = []
resultados = []
v1 = 0
v2 = 0
empate = 0



while True:
    j1 = valida_int("Escolha sua jogada: ", 0, 3)
    if not j1: 
        break
    j2 = random.randint(1,3) # Gera um int aleatório de 1 até 3
    jogadas.append([j1, j2])
    resultados = vencedor(j1, j2)

for jogada in jogadas:
    for dado in jogada:
        print (dado, end = ' ')
    print()

print(f"Número de vitórias do jogador 1: {resultados[0]}")
print(f"Número de vitórias do jogador 2: {resultados[1]}")
print(f"Número de empates: {resultados[2]}")
