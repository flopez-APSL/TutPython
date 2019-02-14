frase = 'La fuerza está en el interior.'



print(frase[:7])
print(frase[7:])

# sustituyendo valores.

letters = ['a','b','c','d','e','f']
print(letters)
# hay que añadir un valor más de distancia.
letters[1:3] = ['B','C']
print(letters)

numbers = [1, 2, 3, 4, 5]

join = [numbers + letters]
separate = [numbers, letters]
print('unido ', join)
print('separado ',separate)
print(separate[0])
print(separate[1])

a, b = 0, 1

def fibonnacci():
    global a, b
    r = input('introduzca el límite del fibonacci: ')
    while a < int((r)):
        print(a)
        a, b = b, a + b

fibonnacci()



