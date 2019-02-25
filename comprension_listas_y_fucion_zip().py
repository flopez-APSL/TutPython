from math import pi
print('Podemos crear una función que nos devuelva los primeros números cuadrados así: ')


def squares(number):
    result = []
    for x in range(number):
        result.append(x**2)

    return result

print(squares(10))

print('O podemos usar la comprensión de listas para ello: ')

square = [x**2 for x in range(10)]
print(square)

print('Se pueden hacer cosas increibles. Vamos a combinar dos listas con un condicional')
combinacionlistas = [(a, b) for a in [1, 2, 3, 4, 5, 6, 7, 8] for b in [1, 5, 8, 4, 2, 8] if a == b]
print(combinacionlistas)

print('Aplicar funciones y crear tuplas con dos valores: ')
eliminando_espacios = ['  banana    ', '  loganberry ', 'passion fruit  ']
result = [x.strip() for x in eliminando_espacios]
print(result)
numero_con_su_cuadrado = [(x, x**2) for x in range(1, 11)]
print(numero_con_su_cuadrado)

decimalesPi = [str(round(pi, i)) for i in range(1, 10)]
print(decimalesPi)

print('-------------------------------ANIDAMIENTO DE LISTAS----------------------')

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          ]

# comoda forma de recorrer un array bidimensional.
transpose = [[row[i] for row in matrix] for i in range(4)]
print(transpose)

# lo anterior es igual a esto:
transposed = []
for i in range(4):
    result = []
    for row in matrix:
        result.append(row[i])
    transposed.append(result)

print(transposed)

# el asterisco disgrega la array bidimensional en listas iterables.
zipeando = list(zip(*matrix))

print(zipeando)

# para verlo mejor:
sin_asterisco = list(zip(matrix[0], matrix[1], matrix[2]))

print(sin_asterisco)

