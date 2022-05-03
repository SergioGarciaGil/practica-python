menu = """
Bienvenido al conversor de monedas💲

1- Pesos colombianos
2- Pesos argentinos
3- Pesos mexicanos

Elige una opción: """

option = int(input(menu))

if option == 1:
    pesos = input("Cuantos pesos colombianos tines?: ")
    pesos = float(pesos)   
    valor_dolar = 3874.10
    dolares = pesos / valor_dolar;
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")

elif option == 2:
    pesos = input("Cuantos pesos Argentino tines?: ")
    pesos = float(pesos)   
    valor_dolar = 65.36
    dolares = pesos / valor_dolar;
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")

elif option == 3:
    pesos = input("Cuantos pesos mexicanos tines?: ")
    pesos = float(pesos)   
    valor_dolar = 24.55
    dolares = pesos / valor_dolar;
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")

else:
    print("Opción inválida")



