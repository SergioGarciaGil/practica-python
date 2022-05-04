def conversor(tipo_pesos, valor_dolar):
    pesos = input("Cuantos pesos " + tipo_pesos + "tienes?: ")
    pesos = float(pesos)
    dolares = pesos/valor_dolar
    dolares = round(dolares,2)
    dolares= str(dolares)
    print("Tienes " + dolares + " dolares")

menu = """
Bienvenido al conversor de monedas💲

1- Pesos colombianos
2- Pesos argentinos
3- Pesos mexicanos

Elige una opción: """

option = int(input(menu))

if option == 1:
    conversor("colombianos", 3875)
elif option == 2:
    conversor("argentinos", 65)

elif option == 3:
    conversor("mexicanos", 24.5)

else:
    print("Opción inválida")



