#Enunciado: Você e sua equipe de programadores foram contratados para desenvolver um app de vendas para uma loja que vende Açaí e Cupuaçu. Você ficou com a parte de desenvolver a interface do cliente para retirada do produto. A Loja possui seguinte relação:

#Tamanho P de Cupuaçu (CP) custa 9 reais e o Açaí (AC) custa 11 reais;
#Tamanho M de Cupuaçu (CP) custa 14 reais e o Açaí (AC) custa 16 reais;
#Tamanho G de Cupuaçu (CP) custa 18 reais e o Açaí (AC) custa 20 reais;

# Menu de boas vindas
print ("   Bem-vindo à loja de Gelados da Ana Clara  ")
print ("---------------- Cardápio -------------------")
print ("---------------------------------------------")
print ("--- | Tamanho | Cupuaçu (CP) | Açaí (AC) |---")
print ("--- |    P    |   R$ 9.00    | R$ 11.00  |---")
print ("--- |    M    |   R$ 14.00   | R$ 16.00  |---")
print ("--- |    G    |   R$ 18.00   | R$ 20.00  |---")

#Acumulador para somar valores dos pedidos
total = 0

# Loop de repetição
while True:
    sabor = input ("Por favor, insira o sabor (CP/AC): ") # Captura o sabor escolhido
    
    if sabor.upper() not in ['CP', 'AC']: # Determina que só vai aceitar esses caracteres e em maiúsculo
        print("Sabor inválido. Tente novamente.")
        continue # Reinicia o if, caso o valor inserido seja inválido

    tamanho = input("Por favor, insira o tamanho (P/M/G): ") # Captura o tamanho escolhido
    
    if tamanho.upper() not in ['P', 'M', 'G']: # Determina que só vai aceitar esses caracteres e em maiúsculo
        print ("Tamanho inválido. Tente novamente.")
        continue # Reinicia o if, caso o valor inserido seja inválido

    # If/elif que determina o preço de cada sabor e tamanho
    if sabor.upper() == 'CP':
        if tamanho.upper() == 'P':
            total += 9
        elif tamanho.upper() == 'M':
            total += 14
        else:
            total += 20
    else:
        if tamanho.upper() == 'P':
            total += 11
        elif tamanho.upper() == 'M':
            total += 16
        else:
            total += 20

    continuar = input ("Deseja pedir mais alguma coisa? Digite 'sim' para continuar): ") # Captura um input que dita se o loop while continuará ou não

    if continuar.lower() != 'sim':
        break

print (f"Total do pedido: R$ {total:.2f}") # Exibe o valor final e total do pedido


