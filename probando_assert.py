
# no usar assert con parentesis porque la convierte en una tubla. Y una tupla con contenido siempre
# es verdadera
#assert(2 + 2 == 5, "Houston we've got a problem")

# dispara un AssertionError si la sentencia no es verdadera.
# cambia el resultado de la suma y lo comprobarás.
assert 2 + 2 == 4, "Houston we've got a problem"




# Imagina que llamas a una función de la que sabes que jamás retorna un valor negativo,
# y usas su respuesta como parte de otra operación:



# a = otra_funcion()
# return 1 + a

# Insisto, la otra_funcion() jamás retornará un negativo.
# Si lo hiciera estaría mal. Pero no te fías del todo, pues quizás esa función no ha sido escrita por ti
# y quizás en una actualización posterior de la librería que la incluye
# aparece un bug y retorna un negativo.
# assert te permite expresar una condición que ha de ser cierta siempre,
# ya que de no serlo se interrumpirá el programa. Podríamos añadir assert así:

def mifuncion(otra_funcion):
    a = otra_funcion
    assert a >= 0, 'ha entrado un numero negativo'        # Asegurarse de que es positivo
    return a + 1

#
# Un detalle importante es que el assert
# debe usarse para cazar condiciones que no deberían ocurrir jamás,
# y si ocurren deben considerarse un error de programación.


# por tanto se pueden usar para generar test. vamos a testear una funcion
# que da la raiz cuadrada.

#resultado = raiz_cuadrada(25)

#assert resultado == 5.0

# Cuando ejecutas estos test desde un entorno de automatización de pruebas,
# ese entorno va capturando los AssertionError que se produzcan,
# de modo que al final puede darte un informe de cuántos test han fallado
# (y cuáles), para que revises la función que no se comportaba como esperabas.
#
# El testing es muy importante durante el desarrollo, pues si modificas la función raiz_cuadrada()
# para corregir un bug que tenía, quieres estar seguro de que no has introducido otro bug al hacerlo.
# El tener una buena batería de tests y que sigan pasando todos después de haber modificado el código
# es fundamental.

# Pon a prueba lo dicho introduciendo un valor negativo a la supuesta funcion del ejemplo.

otra_funcion = 0

mifuncion(otra_funcion)

