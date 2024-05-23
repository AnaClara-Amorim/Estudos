# Crie um programa para ler o nmome de nascimento de diferentes pessoas. Armazene os dados em um dicionário com listas. Ao encerrar, exiba: O total de cadastros efetuados, a médida das idades, uma lista com mulheres com menos de 30 anos, uma lista de homens com idade acima da média. 

cadastro = {'Nome':[], 'Sexo':[], 'Ano':[]}

while True:
    terminar = input("Deseja cadastrar uma pessoa? [S/N]")
    if terminar.upper() in "N":
        break
    if terminar.upper() not in 'S':
        print('Digite S para SIM ou N para NÃO.')
        continue

    nome = input("Qual o nome? ")
    sexo = input("Qual o sexo? ")
    ano = input("Qual o ano de nascimento? ")
    cadastro['Nome'].append(nome)
    cadastro['Sexo'].append(sexo.upper())
    cadastro['Ano'].append(ano)

print(cadastro)

  