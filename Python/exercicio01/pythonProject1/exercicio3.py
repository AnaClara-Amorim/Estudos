frase = (input("Insira uma frase: "))
tam = len(frase) #len vem de lenght, pega o tamanho da string

frase2 = frase[0:int(tam/2)] #A frase dois vai ser escrita de acordo com o tamanho especificado do índice
#0 para pegar do primeiro tam/2 com int antes para evitar numeros racionais

#imprimindo metade
print(frase2)

#imprimindo os dois ultimos caracteres
print(frase[-2]) #o python permite pegar os dois ultimos