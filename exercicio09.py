month = int(input("Digite um número correspondente ao mês: "))

if month < 1 and month > 12:
    print("valor invalido")
else:
    if month == 1:
        print("Janeiro")
    elif month == 2:
        print("Fevereiro")
    elif month == 3:
        print("Março")
    elif month == 4:
        print("Abril")
    elif month == 5:
        print("Maio")
    elif month == 6:
        print("Junho")
    elif month == 7:
        print("Julho")
    elif month == 8:
        print("Agosto")
    elif month == 9:
        print("Setembro")
    elif month == 10:
        print("Outubro")
    elif month == 11:
        print("Novembro")
    else:
        print("Dezembro")


