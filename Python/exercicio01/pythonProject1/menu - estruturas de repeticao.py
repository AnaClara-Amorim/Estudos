print ("Lanchonete")
print ("1 - Coxinha - R$ 2")
print ("2 - Pastel - R$ 7")
print ("3 - Suco - R$ 4")
print ("4 - Bolo - R$ 5")
print ("5 - Sair")

total = 0

while True:
    op = int(input("Qual item gostaria de comprar? "))
    qtd = int(input("Quantas unidades? "))

    if (op == 1):
        total = total + qtd * 2.00
    elif (op == 2):
        total = total + qtd * 7.00
    elif (op == 3):
        total = total + qtd * 4.00
    elif (op == 4):
        total = total + qtd * 5.00
    elif (op == 5):
        break
    else:
        print ("Produto inválido, selecione outro.")

print (f"O total é de R$ {total}")

