#Escreva um algoritmo em python em que o usuário escreve se quer comprar maçãs, laranjas ou bananas. Deverá ser apresentado na tela um menu com as opções. Depois, deve se esoclher quantas unidades e o preço a se pagar. 

print( """MENU
    Escolha o que deseja comprar:
    1 - Maçã
  nja
    3 - Banana""")

qtd ()

match (produto):
    case 1:
        pagar = qtd * 2.3
        print(f'Você comprou {qtd} em maçã. Total a pagar: {pagar}')
    case 2:
        pagar = qtd * 3.6
        print(f'Você comprou {qtd} em laranjas. Total a pagar: {pagar}')
    case 3: 
        pagar = qtd * 1.85
        print(f'Você comprou {qtd} em bananas. Total a pagar: {pagar}')
    case _: 
        print('Produto inexistente!')

