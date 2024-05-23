# STRINGS - são imutáveis

s1 = "Lógica de Programação e Algoritmos"
s1 = list("Algoritmos")
print(s1) #print separado
print (''.join(s1)) #print agrupado
s1[0] = 'a'
print(''.join(s1))

s2 = "Lógica de Programação e Algoritmos"
print(s2.lower().count('a'))
print(s2.count('a')) 

for i in range (10, 20):
    for j in range (10, 20, 2):
        print ('{} + {} = {}'.format(i, j, i + j))


