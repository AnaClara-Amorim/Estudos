#Você foi contratado para desenvolver um sistema de cobrança de serviços de uma copiadora. Você ficou com a parte de desenvolver a interface com o funcionário.

# Parte do código com as funções

# FUNÇÃO DE ESCOLHA DE SERVIÇO
def escolha_servico():
    # LAÇO DE REPETIÇÃO
    while True:
        # Solicita o tipo de serviço desejado
        servico = input("Entre com o tipo de serviço desejado \nDIG - Digitalização \nICO - Impressão Colorida \nIPB - Impressão Preto e Branco \nFOT - Fotocópia \n>>").upper()

        # Ifs com a atribuição do valor de cada serviço
        if servico == "DIG":
            return 1.10 
        elif servico == "ICO":
            return 1.00
        elif servico == "IPB":
            return 0.40
        elif servico == "FOT":
            return 0.20
        else:
            print("Escolha inválida, entre com o tipo de serviço novamente.")  # Mensagem de erro para escolha de serviço inválida

# FUNÇÃO DE NÚMERO DE PÁGINAS
def num_pagina():
    # LAÇO DE REPETIÇÃO
    while True:
        # Try para tratamento de dados 
        try: 
            # Solicita o número de páginas
            paginas = int(input("Entre com o número de páginas: \n>> "))
            if paginas > 20000:
                print("Não aceitamos tantas páginas de uma vez.")  # Mensagem de erro para número de páginas inválido
            # Descontos calculados em cima do número de páginas
            else:
                if paginas < 20: # Não aplica desconto
                    return paginas
                elif 20 <= paginas < 200:
                    return paginas * 0.85  # Aplica 15% de desconto
                elif 200 <= paginas < 2000:
                    return paginas * 0.80  # Aplica 20% de desconto
                elif 2000 <= paginas < 20000:
                    return paginas * 0.75  # Aplica 25% de desconto
        except ValueError: 
            print("Por favor, entre com o número de páginas novamente.")  # Mensagem de erro para entrada não numérica

# FUNÇÃO DE SERVIÇO EXTRA
def servico_extra():
    # LAÇO DE REPETIÇÃO
    while True:
        # Try para tratamento de dados 
        try:
            # Solicita o serviço adicional desejado
            extra = int(input("Deseja adicionar algum serviço? \n1 - Encadernação Simples - R$ 15.00 \n2 - Encadernação Capa Dura - R$ 40.00 \n0 - Não desejo mais nada \n>>"))
            if extra == 1:
                return 15
            elif extra == 2:
                return 40
            elif extra == 0:
                return 0
            else:
                print("Opção inválida, por favor escolha entre 1, 2 ou 0.")  # Mensagem de erro para escolha de serviço adicional inválida
        except ValueError:
            print("Por favor, insira um número válido.")  # Mensagem de erro para entrada não numérica

# Parte do código principal
print("Bem-vindo à copiadora da Ana Clara")

servico = escolha_servico() # Atribui a serviço o retorno da função escoha_servico

paginas = num_pagina()

extra = servico_extra()

# Calcula o valor total a ser pago
total = (servico * paginas) + extra

# Mensagens finais
print(f"Serviço escolhido: {'DIG' if servico == 1.10 else 'ICO' if servico == 1.00 else 'IPB' if servico == 0.40 else 'FOT'}") # Esses ifs e else estão ajudando a retornar o tipo de serviço escolhido pelo usuário, não o que é retornado pela função "escolha_serviço"
print(f"Número de páginas (após desconto): {paginas}")
print(f"Serviço adicional: {'Encadernação Simples' if extra == 15 else 'Capa Dura' if extra == 40 else 'Nenhum'}") # Esses ifs e else estão ajudando a retornar o tipo de serviço adicional escolhido pelo usuário, não o que é retornado pela função "servico_extra"

# Mostra o total a se pagar
print(f"Total a pagar: R${total:.2f}")
