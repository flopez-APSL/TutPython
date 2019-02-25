def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

countdown = [1,2,3,4,5,6,7,8,9,10]


for char in reverse(countdown):
    print(char)


# se puede hacer lo anterior, de una forma más sencilla aún.
# como si fuese una comprensión de listas, pero usando ()
result = list(countdown[i] for i in range(len(countdown)-1, -1, -1))
print(result)

#otros ejemplos
suma_cuadrados = sum(i*i for i in range(10))                 # sum of squares
print(suma_cuadrados)
xvec = [100, 200, 300]
yvec = [1, 2, 3]
producto = sum(x*y for x,y in zip(xvec, yvec))         # dot product
print(producto)


