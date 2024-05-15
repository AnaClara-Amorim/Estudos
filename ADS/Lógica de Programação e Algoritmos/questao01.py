#Enunciado: Imagina-se que você é um dos programadores responsáveis pela construção de app de vendas para uma determinada empresa X que vende em atacado. Uma das estratégias de vendas dessa empresa X é dar desconto maior conforme o valor da compra, conforme a listagem abaixo:

#Se valor for menor que 2500 o desconto será de 0%;
#Se valor for igual ou maior que 2500 e menor que 6000 o desconto será de 4%;
#Se valor for igual ou maior que 6000 e menor que 10000 o desconto será de 7%;
#Se valor for igual ou maior que 10000 o desconto será de 11%;

print("Bem-vindo a Loja da Ana Clara")
valor_produto = int(input("Entre com o valor do produto: ")) # Coleta o valor do produto
qnt_produto = int(input("Entre com a quantidade do produto: ")) # Coleta a quantidade do produto

total = valor_produto * qnt_produto # Calcula o valor total da compra

if total <= 2500: # Aplica o desconto no caso de compra menor que 2500
    desconto = 0
    valor_com_desconto = total
else: 
    if total < 6000: # Valor do desconto no caso de compra menor que 6000 e maior que 2500
        desconto = 0.04
    elif total < 10000: # Valor do desconto no caso de compra menor que 10000 e maior que 6000
        desconto = 0.07
    else: 
        desconto = 0.11 # Valor do desconto para comprar maiores de 10000

valor_com_desconto = total - (total * desconto) # Aplica o valor do desconto à compra

print(f"O valor SEM desconto: {total}") # Exibe o valor sem desconto
print(f"O valor COM desconto: {valor_com_desconto}") # Exibe o valor com desconto