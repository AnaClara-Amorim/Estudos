# Estrutuda de dados é um conjunto de dados organizados e uma maneira especifica na memória do programa.

# A TUPLA () é uma estrutura estática de dados, uma vez alocada na memória, não pode mais ter seu endereçamento alterado. 

mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
print(mochila)
print(mochila[1]) # Print do elemento 1
print(mochila[0:2]) # Print do índice 0 até 1
print(mochila[2:]) # A partir do índice 2
print(mochila[-1]) # ultimo elemento

# mochila [2] = 'Ovos', caso isso fosse feito, não haveria atribuição, pois a tupla é imutável

for item in mochila:
    print(f'Na minha mochila tem: {item}')

# ou

tam = len(mochila)
for i in range (0, tam, 1):
    print (f'Na minha mochila tem: {mochila[i]}')

upgrade = ('Queijo', 'Canivete')
mochila_grande = mochila + upgrade
print (mochila_grande)

# Desempacotamento de parâmetros em funções
#Suponhamos que queremos realizar o somatório de diversos valores, porém não sabemos quantos valores serão somados. Pode ser que sejam somente 2, ou então 10, ou mesmo 100 números

def soma(*num): # Esse asterístico é uma tupla de tamanho qualquer
    acumulador = 0
    print('Tupla: {}'.format(num))
    for i in num:
        acumulador += i
    return acumulador
#Programa principal
print(f'Resultado: {soma(1,2)}\n')
print(f'Resultado: {soma(1,2,3,4,5,6,7,8,9)}\n')

linguagens = ('Javascript', 'Rust', 'Swift', 'Python', 'Kotlin',  'Go', 'C#', 'Dart','Julia', 'Typescript')
i = 0
while (linguagens[i] != 'Python'):
 i += 1
print(f'Encontramos Python na {i + 1} posição!')