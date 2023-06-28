import random

def adivina_el_numero(a,b):
    print("========================")
    print("Bienvenido al Juego!")
    print("========================")
    print()
    print("Su objetivo es adivinar el numero elegido por la computadora. Comencemos!")

    numero_aleatorio = random.randint(a,b)
    return numero_aleatorio

a = int(input("Ingrese el comienzo de un intervalo de numeros: "))
b = int(input("Ingrese el final del intervalo: "))
num_random = adivina_el_numero(a,b)
prediccion = None
contador = 0
while prediccion != num_random:
    prediccion = int(input(f"Ingrese su prediccion al numero entre {a} y {b}."))
    contador += 1
    if prediccion != num_random:
        if abs(prediccion - num_random) > 10:
            print("Diria que bastante alejado...")
            
        elif abs(prediccion - num_random) > 3:
            print("Casi!! Estuviste cerca!")
        else:
            print("Estas que quema!! Vas por el camino correcto.")
print(f"Correcto!!Felicidades, acertaste y te llevo {contador} intentos.")


