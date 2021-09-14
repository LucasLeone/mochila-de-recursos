"""
    Determinar la palabra mas grande
    (indicar criterios)
"""

print('El criterio para determinar la palabra mas grande es por la cantidad de letras.')

texto = input('Ingrese un texto: ')

palabras = texto.split(' ')
mayor = 'a'

for i in range(0, len(palabras)):

    if i == 0:
        mayor = palabras[0]

    if len(palabras[i]) > len(mayor):
        mayor = palabras[i]

print(f'La palabra mayor es: {mayor}')