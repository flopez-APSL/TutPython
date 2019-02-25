"""

Herramientas de medición de tiempos de ejecución
decódigo.

"""

import cProfile, pstats  # modulo para hacer estadisticas e imprimir los datos.

cProfile.run('for x in range(1000):print(x* x + 1)')

"""
Primeramente, indica el número de llamadas recursivas y primitvas (No recursivas)

Estadisticas:

ncalls: numero de llamadas

tottime: tiempo total empleado en la función.

percall: es el cociente de tottime dividido por ncalls

cumtime: es el tiempo acumulado empleado en esta y todas las subfunciones (
desde la invocación hasta la salida). Esta cifra es precisa incluso para funciones recursivas.

percall: es el cociente de cumtime dividido por llamadas primitivas
"""

