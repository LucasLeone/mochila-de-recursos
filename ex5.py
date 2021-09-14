"""
    Buscar una subcadena dentro de una cadena
"""

cadena = input('Ingrese una cadena: ')

subcadena = input('Ingrese la subcadena a buscar: ')

if subcadena in cadena:
    print('Si se encuentra dentro de la cadena!')
else:
    print('No se encuentra dentro de la cadena :c')