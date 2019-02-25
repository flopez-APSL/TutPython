# bucle clásico.
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)


# creando un objeto iterador
s = 'abc'
it = iter(s)
it

try:
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
except (StopIteration):
    print('Fin de la iteracción')


class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data) # recoje el tamaño del data.

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('Vamos a ver como funciona')

for char in rev:
    print(char)


