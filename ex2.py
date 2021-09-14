"""
    Determinar la cantidad de vocales,
    espacios en blancos y consonantes
    en un texto
"""
VOCALES = ['a', 'e', 'i', 'o', 'u']


cadena = list(input('Ingrese la cadena de caracteres: '))


vocales = 0
blancos = 0
consonantes = 0

for i in cadena:

    if i in VOCALES:
        vocales += 1
    
    if i == ' ':
        blancos += 1

    if i not in VOCALES and i != ' ':
        consonantes +=1

print(f'La cantidad de vocales son: {vocales}')
print(f'La cantidad de espacios en blanco son: {blancos}')
print(f'La cantidad de consonantes son: {consonantes}')