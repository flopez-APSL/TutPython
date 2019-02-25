
def fib(n):
    print('Secuencia de fibonacci entre 0 y ', n)
    a, b = 0, 1
    while a < n:
        print(a, end= ' ')
        a, b = b, a + b

    print()


fib(1000)

# las funciones pueden asociarse como variables.


f = fib # f se comportará como la función fib().

f(10000)


# En éste caso, f recibe el resultado de la función:
def fibreturn(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b

    return result

f = fibreturn(10000)
print('Imprimiendo el array de resultado de la función fibonacci con Return. \n', f)


# parametros por defecto.
def ask_ok(prompt, retries = 4, reminder = 'Please try again'):
    while True:
        ok = input(prompt)
        if ok in ('y','ye','yes'):
            return True
        if ok in ('n','no','nop','nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('BOOM!!!...')
        print(reminder)


print('En esta función pasamos la pregunta como argumento. Siempre. \n'
      ' También podemos pasar la pregunta, y los intentos por argumentos \n'
      'finalmente, podemos pasar la pregunta, y la respuesta en caso de error ')

ask_ok('Sabes escribir yes? ')
ask_ok('Quieres desactivar la bomba? tienes tres intentos: ',3)
ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')


print('Podemos inicializar una lista. De esa forma, la función guardará \n'
      'en ella los datos que se introduzcan como argumento')


def f(a, L =[]):
    L.append(a)
    return 'elementos de la lista: ', L


print(f(1))
print(f(2))
print(f(3))
print(f(5))


print('Creando la función de esta forma, la lista se re-inicializa y no se comparte con la siguiente llamada \n'
      ' No parece que sea muy útil.')


def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


print(f2(1))
print(f2(2, [40, 10, 8]))
print(f2(3))
print(f2(5, [5, 50, 550]))

