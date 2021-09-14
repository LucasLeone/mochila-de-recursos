"""
    Concatenar dos cadenas ingresadas
    por teclado en posiciones indicadas
"""

cadena1 = input('Ingrese una cadena: ')
cadena2 = input('Ingrese otra cadena: ')

pos = int(input('Ingrese la posicion que quiere concatenar la segunda cadena: '))

concatenado = cadena1[0:pos] + cadena2 + cadena1[pos:len(cadena1)]

print(concatenado)