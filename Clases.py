class Persona():
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad =edad

    def __str__(self):
        return 'Me llamo {} {}. Tengo {} años.'.format(self.nombre, self.apellido,self.edad)


yo = Persona('Fernando', 'Lopez', 45)

print(yo)



class Perro:

    familia = 'cánido'         # variable de clase compartida con todas las instancias
    # trucos = []      variable de clase incorrecta. Todos los perros tendrian los mismos
    #trucos.

    def __init__(self, name, raza):
        self.name = name    # variables de la instancia.
        self.raza = raza
        self.trucos = [] # la lista ha de ser nueva para cada perro.

    def aprender_truco(self, trucos):
        self.trucos.append(trucos)

    def __str__(self):
        return 'Me llamo {}. Soy un {} de la raza {}.'.format(self.name, self.familia, self.raza)

Sam = Perro('Sam','Pastor Belga')
Sultan = Perro('Sultan','Pastor Alemán')

print(Sam, Sultan)

Sam.aprender_truco('Coger un frisbee')
Sultan.aprender_truco('Perseguir una pelota')

print(Sam.trucos)







