
print(sorted([5, 2, 3, 1, 4]))

lista = [5, 2, 3, 1, 4]

lista.sort()  # no devuelve una lista ordenada. se ordena a sí misma.

print(lista)

# list.sort() solo ordena listas. sorted(), ordena cualquier iterable.
print(sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}))

# no distingue entre mayusculas y minusculas .lower
strlower = sorted("This is a test string from Andrew".split(), key=str.lower)

print(strlower)

student_tuples = [
    ('John', 'Smith', 15),
    ('Jane', 'Mccloud', 12),
    ('Dave', 'Vanian', 10),
    ]

edad_orden = sorted(student_tuples, key=lambda student: student[2])   # ordenados por edad
print(edad_orden)


class Student:
    def __init__(self, name, secondname, age):
        self.name = name
        self.secondname = secondname
        self.age = age

    def __repr__(self):
        # return repr(self.name)+' '+repr(self.secondname)+' '+repr(self.age)
        # return '{} {} {}'.format(*map(repr, [self.name, self.secondname, self.age]))
        return '{} {} {}'.format(self.name, self.secondname, self.age)


student_objects = [
    Student('john', 'Smith', 15),
    Student('jane', 'Mccloud', 12),
    Student('dave', 'Vanian', 10),
    ]

print('------------------ordenación de objetos---------------------------------')
objects_order = sorted(student_objects, key=lambda student: student.age)   # objetos, ordenados por edad.


print(objects_order)

from operator import itemgetter, attrgetter

print(sorted(student_tuples, key=itemgetter(2)))

print(sorted(student_objects, key=attrgetter('age')))


# varios niveles de ordenamiento. primero por apellido y después por edad.
print(sorted(student_tuples, key=itemgetter(1,2)))

print(sorted(student_objects, key=attrgetter('secondname', 'age')))

sorted(student_tuples, key=itemgetter(2), reverse=True) # descendentemente.

print('-----------------------------------------------------------------------')

data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]

print(sorted(data, key=itemgetter(0))) # respeta las claves repetidas.

# varios ordenamientos.
s = sorted(student_objects, key=attrgetter('age'))     # ordenamos primero por edad ascendente.
print(sorted(s, key=attrgetter('secondname'), reverse=True)) # y el apellido, descendentemente..


