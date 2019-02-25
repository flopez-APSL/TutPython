# creación y des-empaquetamiento de tuplas.
t = 123, 456, 'siete', 'ocho'

print(t)

a, b, c, d = t

print(a, b, c, d)

print('----------------------------CONJUNTOS-------------------------------------------')
a = {1, 2, 3, 4, 5}

b = {1, 2, 3, 6, 7}

# elimina los elementos en a que estén en b.
c = a - b
print(c)

# union de conjuntos, evidentemente sin repetir los objetos comunes.
c = a | b
print(c)

# elementos en comun de ambos conjuntos.
c = a & b
print(c)

# devuelve un conjunto con los elementos NO COMPARTIDOS en cada conjunto.
c = a ^ b
print(c)

print('-------------------COMPRENSION DE CONJUNTOS---------------------------------')

facturas_pendientes = {'FA00982', 'FA00983', 'FA00984', 'FA00985', 'FA00986'}
facturas_cobradas = {'FA00982', 'FA00986'}

facturas_pendientes = {x for x in facturas_pendientes if x not in facturas_cobradas}

print(facturas_pendientes)

print('----------------------DICCIONARIOS------------------------------------------')

# creado de forma comprensora
diccionario_numeros_al_cubo = {x: x**2 for x in (1, 2, 3, 4, 5, 6, 7)}
print(diccionario_numeros_al_cubo)

directamente = dict(capital1=4139, capital2=4127, capital3=4098)
print(directamente)

clientes = ['Amazon', 'Google', 'Microsoft', 'Oracle']
cuentas = ['00011101', '991000111', '119191111', '119981911']

clientes_cuentas = dict(zip(clientes, cuentas))

print(clientes_cuentas)







