


words = ['hola', 'mundo', 'Quiero salir antes del hola mundo', '.']

words2 = ['hola', 'mundo', 'Quiero salir antes del hola mundo', '.']

words3 = ['hola', 'mundo', 'Quiero salir antes del hola mundo', '.']



# diferencias entre un for con [:] y lo mismo sin  el.
# realiza una copia y no genera la introducción del dato en la lista iterada.
print('lista antes del bucle: ',words)

for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)     # el cero es el indice.

print('lista despues del bucle iterada con copia', words)

print('hagamos lo mismo sin colocar [:] ')
# Si no colocamos el [:] al insertar en la misma lista que iteramos, desplazamos el indice.
#De esta forma nos quedamos en el mismo sitio y el bucle no avanza..
for z in words2:
    if len(z) > 6:
        words2.insert(0, z)
        print(words2, end= ' sin [:] \n')
        respuesta = input('Esto es un bucle infinito porque la lista corre un puesto \n'
                          'en cada insercción. [intro: continua] [Teclea otra letra para salir del bucle] -> ')
        if respuesta:
            break

print('Una forma de evitarlo es usando el indice como iterador. Como si fuese un bucle en Java. ')
vez = 0
for z in range(len(words3)):
    print('indice: ', z)
    if len(words3[z]) > 6:
        words3.insert(0, words3[z])
        vez += 1
        print('vez: ', vez)
        # print(words3, end= ' sin [:] y con indice \n')
        # respuesta = input('Si pulsas intro entrarás una vez más al bucle. si pulsas una letra \n'
        #                   'saldras ahora mismo. [INTRO: compruebalo. ]')
        #
        # if respuesta:
        #     break

print('lista manejada con índice ',words3)
# imprimiendo con la funcion len() en range


#impresión de índice y valor.
print('imprimimos un array con sus indices. ')
a = ['a','b','c','d','e','f']

for i in range(len(a)):
    print(i, a[i])



