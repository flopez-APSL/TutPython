print('----------------manejando argumentos varios-------------------')


def concatenar(*args, sep = '/'):
    return sep.join(args)


print(concatenar("earth", "mars", "venus"))
print(concatenar("earth", "mars", "venus", sep="."))

# des-empaquetando.


def numerosentre(a, b):
    print('lista de numeros entre ', a, ' y ', b)
    args = [a, b]
    print(list(range(*args)))


numerosentre(34, 43)

print('-----------------------------funciones anónimas lambda-----------------------')

# En este ejemplo tenemos una
# funcion que genera OTRA FUNCION que incrementa un valor con el anterior valor determinado
# con la funcion lambda.. ..jo que lio!!


def make_incrementor(n):
    return lambda x: x + n

print('creamos la función incrementadora con el numero 12')
f = make_incrementor(12)
print('la usamos con el valor 10. Resultado:')
print(f(10))
print('creamos la función incrementadora con el numero 11')
f = make_incrementor(11)
print('la usamos con el valor 1. Resultado:')
print(f(1))
print('la función incrementadora con un valor negativo, (-50)')
f = make_incrementor(-50)
print('introducimos 100. Resultado:')
print(f(100))

print('........................Ordenando una lista numéricamente o Alfabéticamente.........')
pairs = [(3, 'tres'), (2, 'dos'), (1, 'uno'), (4, 'cuatro')]

print('Numericamente: ')
pairs.sort(key=lambda x: x[0])
print(pairs)

print('Alfabéticamente: ')
pairs.sort(key=lambda x: x[1])
print(pairs)

print('Ejemplo de ordenamiento de una lista por tamaño. Usando la función sort(). No hay lambda aquí.')
lista = ['11','23433','kjhfdkjahsdfksaj','32']

lista.sort(key=len)
print(lista)















