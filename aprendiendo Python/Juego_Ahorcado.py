import random

import string

from ahorcado_diagrama_vidas import dic_de_vidas

def obtener_palabra(x):
    palabra = random.choice(x)
    return palabra.upper()

def ahorcado():

    print()
    print("==================================")
    print("Bienvenido al Juego del Ahorcado!")
    print("==================================")
    print()
    print("Su objetivo es adivinar la palabra y perder la menor cantidad de vidas posibles.")
    print()
    print("Elija su dificultad:")
    print("Facil - Medio - Dificil")
    eleccion = input("Ingrese su eleccion: ")
    eleccion = eleccion.lower()

    while not(eleccion == "facil" or eleccion == "medio" or eleccion == 'dificil'):
        eleccion = input("Ingrese una dificultad valida!...")

    palabras_facil = ["perro" , "gato" , "lobo" , "rinoceronte" , "buho" , "anteojos" , "ojos" , "teclado" , "queso" , "tomate" , "salame" , "mate"]
    palabras_medio = ["computadora" , "estrellas" , "murcielago" , "gimnasio" , "serpiente" , "riquelme" , "messi" , "planeador"]
    palabras_dificil = ["terminal" , "python" , "escuela" , "auriculares" , "estreptococo" , "salmonela" , "tenis" , "muay thay" , "usuario"]
    

    if eleccion == "facil":
        palabra = obtener_palabra(palabras_facil)
    elif eleccion == "medio":
        palabra = obtener_palabra(palabras_medio)
    else:
        palabra = obtener_palabra(palabras_dificil)
    
    letras_por_adivinar = set(palabra)
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase)

    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f"Te quedan {vidas} vidas y has usado las siguientes letras: {'-'.join(letras_adivinadas)}") 

        #Mostrando el estado actual de la palabra
        palabra_lista = []
        for letra in palabra:
            if letra in letras_adivinadas:
                palabra_lista.append(letra)
            else:
                palabra_lista.append("-")
        print(dic_de_vidas[vidas])
        print(f"{' '.join(palabra_lista)}")
        
        
        letra_usuario = input("Ingrese su letra: ").upper()

        #Si la letra elegida por el usuario esta en el abecedario y 
        # no esta en el conjunto de letras ya adivinadas, 
        # se la aniade al conjunto.
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)
            
            #Si la letra en palabra, quitar la letra del conjunto de letras 
            # pendientes por adivinar, caso contrario restar una vida.
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print()
            else:
                vidas -= 1
                print(f"\nLa letra {letra_usuario} no esta en la palabra.")
        #Si la letra elegida ya fue ingresada.
        elif letra_usuario in letras_adivinadas:
            print("\nEsa letra ya fue seleccionada, escoge una nueva.")
        else:
            print("\nEsta letra no es valida")
    if vidas == 0:
        print(dic_de_vidas[vidas])
        print(f"\nAhorcado! Perdiste... La palabra era {palabra}")
    else:
        print(f"\nFelicidades! Adivinaste la palabra! {palabra}")

ahorcado()