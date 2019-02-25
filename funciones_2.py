

# practicando funciones con diferentes parametros.
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot(2,action = 'eat soup')
parrot(10000)
parrot(23000,type = 'Loro españó')
parrot(23000000,state= 'deaddddd!!!')

print('--------------------Argumentos con * y **----------------------------- \n')


def tipos_argumentos(soyloprimero, *todo_lo_posterior, **keywords):
    print('Este es el argumento sin asteriscos:', soyloprimero)
    print('argumentos con un *: ')
    for arg in todo_lo_posterior:
        print(arg)
    print('Y todo esto, son keywords: ')
    for kw in keywords:
        print(kw, ":", keywords[kw])


tipos_argumentos('soy el primero.','En teoria, ','estas tres cadenas',
                 'van "a lo posterior".', diccionario={'Fernando': 'Lopez', 'Antonio': 'Gonzalez'},
                 keywords='A ver, a ver...')


tipos_argumentos(1, 2, 3, 4, 5, 6, 7, 8, nueve={9: 'nueve'}, diez=(10, '10'), once=11)

file = open('textfile.txt', 'w')

file.write('Hello World \n')
file.write('Otra linea mas \n')
file.write('and this is another line \n')


def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))


write_multiple_items(file, ' ', 'En un lugar de la mancha ','cuyo nombre no me ',
                     'quiero acordar.. ', 'vivía un hidalgo caballero llamado: ', 'Don Quijote')

file.close()

