class Persona:

    def __init__(self) -> None:
        print('Soy una persona')


class Pepe(Persona):

    def __init__(self, nombre='pepe'):
        self.nombre = nombre
        super().__init__()

    def __str__(self):
        return '{} {}'.format(self.__class__,self.nombre)

pepe = Pepe('Pepito')

print(pepe)

pepe

