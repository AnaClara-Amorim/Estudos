valor = int(input("Digite o valor em reais: "))

while True:
    if valor >= 100:
        cont100 = valor // 100 # com duas barras elimina as casas
        valor = valor - cont100 * 100
        print (f"Cédulas de 100 serão: {cont100}")
        if not valor:
            break

    if valor >= 50:
        cont50 = valor // 50
        valor = valor - cont50 * 50
        print (f"Cédulas de 50 serão: {cont50}")
        if not valor:
            break

    if valor >= 20:
        cont20 = valor // 20
        valor = valor - cont20 * 20
        print (f"Cédulas de 20 serão: {cont20}")
        if not valor:
            break

    if valor >= 10:
        cont10 = valor // 10
        valor = valor - cont10 * 10
        print (f"Cédulas de 10 serão: {cont10}")
        if not valor:
            break

    if valor:
        cont1 = valor
        print(f"Cédulas de 1: {cont1}")
        break