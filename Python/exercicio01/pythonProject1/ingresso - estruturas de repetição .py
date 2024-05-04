total = 0
dinheiro = 0
acc_idades = 0

while True:
    idade = int(input("Qual sua idade? "))

    if idade == 0:
        break
    total +=1
    acc_idades += idade

    if idade > 3:
        print ("Ingresso gratuito!")
        ingresso = 0
    else:
        if idade > 12:
            ingresso = 30
        else:
            ingresso = 15

    dinheiro += ingresso #dinheiro = dinheiro + ingresso

if total > 0:
    media = idade / total
    print (f"Total de pessoas: {total} ")
    print (f"Total arrecadado: {dinheiro}")
    print (f"Média arrecadada {media}")