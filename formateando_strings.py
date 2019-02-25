elecciones = 'Elecciones Generales'
fecha = '26 de Abril de 2019'

print(f'Resultados de las {elecciones} celebradas el {fecha}')


yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)

# después de :. el primer numero el espacio reservado en digitos.
# el segundo numero, el número de decímales.
print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))


import math
print(f'The value of pi is approximately {math.pi:.3f}.')

table = {'Fernando': 622545823, 'Marcos': 6523258541, 'María': 633322365}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

# imprimiendo con comillas.
animals = 'eels'
print(f'My hovercraft is full of {animals}.')
print(f'My hovercraft is full of {animals!r}.')

