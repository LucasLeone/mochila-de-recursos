"""
    Eliminar una cadena dentro de un texto.
"""

texto = list(input('Ingrese un texto: '))

cadena = list(input('Ingrese la cadena a eliminar: '))

for i in range(0, len(texto)):

    if texto[i] in cadena:
        texto[i] = ''


final = ''

for i in texto:
    final += i

print(final)