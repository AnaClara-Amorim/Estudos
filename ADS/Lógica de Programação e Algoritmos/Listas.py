# LISTAS[]. Ao contrário das tuplas, é possível altarar seus dados. 

mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
print (mochila)
mochila[2] = 'Laranja'
print ("Lista: ", mochila)

mochila.append('Ovos') # Adiciona no final da lista
print("Lista: ", mochila)

mochila.insert(1, 'Canivete') #Insere na posição informada
print('Lista: ', mochila)

# FORMAS DE REMOÇÃO
del mochila[1]
print("Lista: ", mochila)

mochila.remove("Ovos")
print("Lista: ", mochila)

# CÓPIAS DE LISTAS

#Referenciada
lista_original = [5, 7, 9, 11]
lista_referenciada = lista_original
print(lista_original)
print(lista_referenciada)

# Altera as duas listas
lista_referenciada[0] = 2
print(lista_original)
print(lista_referenciada)

# Cópia de fato: 
lista_original = [5, 7, 9, 11]
lista_referenciada = lista_original[:] # Nesse caso, cria uma cópia na memória
print(lista_original)
print(lista_referenciada)



