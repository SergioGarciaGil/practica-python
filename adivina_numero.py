import random 

def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input('Ingrese un numero del 1 al 100: '))
    while numero_elegido != numero_aleatorio:
        if(numero_elegido < numero_aleatorio):
            print('El numero es mayor')
        else:
            print('El numero es menor')
        numero_elegido = int(input('elige otro 1 al 100: '))
    print('Felicidades, adivinaste el numero!')


if __name__ == '__main__':
    run()
    