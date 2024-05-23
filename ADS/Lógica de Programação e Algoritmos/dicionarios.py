# DICIONÁRIOS {} estrutura dinâmica, assim como as listas.
#Um dicionário contém no seu cerne uma estrutura de dados chamada de  hash. Uma hash é um tipo de estrutura de dados que é capaz de inserir e buscar  dados utilizando chaves (também chamadas de “palavras-chaves”), e não os seus índices.

#Tuplas
mochila = ('Laptop', 'Smartphone', 'Power Bank', 'Carregadores e Cabos') 
print('Tupla: ', mochila)

#Listas
mochila = ['Laptop', 'Smartphone', 'Power Bank', 'Carregadores e Cabos'] 
print('Lista: ', mochila)
#Dicionários
mochila = {'Laptop':1, 'Smartphone':2, 'Power Bank':3, 
'Carregadores e Cabos':4} 
print('Dicionário: ', mochila)

game = {'nome':'Super Mario', 'desenvolvedora':'Nintendo',  'ano':1990} 
print(game)

print(game['nome'])
print(game['desenvolvedora'])
print(game['ano'])

# Métodos para dicionários

print(game.values)
#ou
for values in game.values():
    print(values)

for keys, values in game.items():
    print(f'{keys} = {values}')

# É possível fazer lista com dicionários ou ao contrário

# Lista com dicionários dentro
games = []
for i in range(3):
 game['nome'] = input('Qual o nome do jogo?') 
 game['videogame'] = input('Para qual video game ele foi lançado?') 
 game['ano'] = input('Qual o ano de lançamento?') 
 games.append(game.copy())
print('-' * 20) 
for jogos in games:
    for chave, valor in jogos.items():
        print(f'O campo {chave} tem o valor {valor}.')

# Dicionário com listas dentro

games = {'nome':[],'videogame':[],'ano':[]}
for i in range(3):
 nome = input('Qual o nome do jogo?') 
 videogame = input('Para qual video-game ele foi lançado?') 
 ano = input('Qual o ano de lançamento?') 
 games['nome'].append(nome)
 games['videogame'].append(videogame)
 games['ano'].append(ano)
print('-' * 20) 
print(games)