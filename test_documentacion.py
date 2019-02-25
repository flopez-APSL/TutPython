import doctest


doctest.testmod()

def areaTrianguloconString(base, altura):

    """

    :param base: del triangulo.
    :param altura: del triángulo
    :return: la base de un triángulo

    >>> areaTrianguloconString(3,6)
    'El área del Tríangulo es: 9.0'
    """

    return 'El área del Tríangulo es: '+ str((base * altura) / 2)

doctest.testmod()

