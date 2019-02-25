class Gato(object):

    """
    Clase Gato
    """
    def __init__(self):
        super(Gato, self).__init__()

    def _privado(self):
        """
        Metodo supuestamente privado
        """
        print('Soy privado como los intereses del estado')

    def un_metodo(self):
        """
        Metodo supuestamente público donde se accede al privado
        """
        self._privado()

gato1 = Gato()


print('Accedemos al metodo privado a través del publico')
gato1.un_metodo()








class Gatico(Gato):

    """La clase Gatico hereda de la clase Gato"""
    def __init__(self):
        super(Gatico, self).__init__()

    def _privado(self):
        """Estoy sobreescribiendo el metodo privado?"""

        # super()._privado() con esta instrucción llamamos al metodo privado heredado.
        print("Es necesario abrir los datos al publico y dejar de ser privado…")

    def otro_metodo(self):
        self._privado()

gatito = Gatico()

print('Este gatito no tiene acceso al metodo privado padre, pero si puede sobre-escribirlo')
gatito.otro_metodo()

print('Intenta acceder al metodo privado. ')
gatito.un_metodo()
print('Como ves, accede al suyo. ')



print('------------------------------------------------')
print('Mientras tanto, el gato puede seguir accediendo a su metodo privado')
gato1.un_metodo()
gato2 = Gato()
print('creamos otro objeto Gato y también accede a su metodo privado')
gato2.un_metodo()
print('------------------------------------------------')
gatito2 = Gatico()
print('Terminamos creando otro objeto gatito, que accede a su metodo privado')
gatito2.otro_metodo()
gatito.otro_metodo()








