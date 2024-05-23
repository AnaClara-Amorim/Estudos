# STRINGS E LISTAS DENTRO DE LISTAS

#temos um índicereferente a cada item da lista, e um segundo índice referente a cada caractere da string.
mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
print(mochila[0][0])
print(mochila[2][1]) 

# Vamos criar umalista vazia e ir adicionando um produto por vez nela. O laço de repetição de cadastro possibilita somente 3 itens para fins de simplificação do exercício.

item = []
mercado = []
for i in range(3):
    item.append(input('Digite o nome do item:'))
    item.append(int(input('Digite a quantidade:')))
    item.append(float(input('Digite o valor:')))
    mercado.append(item[:])
    item.clear() # Limpa a variável
print(mercado)

mercado1 = []
for i in range(3):
    nome = input('Digite o nome do item:')
    qtd = int(input('Digite a quantidade:'))
    valor = float(input('Digite o valor:'))
    mercado1.append([nome, qtd, valor])
print(mercado1)
