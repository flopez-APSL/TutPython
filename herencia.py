class Foo:
  a = 5


string = '..'
numero = Foo()
boolean = True
float = 23.67
result = isinstance(numero,int)
result2 = isinstance(string,str)
print('Clase Foo: ',result,'Clase String', result2)


class Polygon:
    def __init__(polygonType):
        print('Polygon is a ', polygonType)


class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__('triangle')


print(issubclass(Triangle, Polygon))
print(issubclass(Triangle, list))
print(issubclass(Triangle, (list, Polygon)))
print(issubclass(Polygon, (list, Polygon)))



# se pueden generar clases vacías.
# después darle atributos y metodos. esto puede generar
# objetos de la misma clase con diferentes caracteristicas.

class Employee:
    pass

john = Employee()

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000

def salarioanual(salary):
    return salary * 12

def vaguear():
    return 'Paso de currar'


john.salarioanual = salarioanual


print(john.name, john.dept, john.salary)

print(john.salarioanual(john.salary))

pepe = Employee()

pepe.vaguear = vaguear

print(pepe.vaguear())

print(isinstance(pepe, Employee))
print(isinstance(john, Employee))

