"""
    Buscar un carácter dentro de una cadena.
"""
import sys

cadena = list(input('Ingrese una cadena: '))

caracter = input('Ingrese el caracter que quiere buscar: ')

if len(caracter) != 1 or caracter == ' ':
    print('Caracter no valido')
    sys.exit()


for i in range(0, len(cadena)):

    if caracter == cadena[i]:
        i += 1
        print('El caracter esta en la posicion:', i)
        sys.exit()