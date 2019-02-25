

# buscando numeros primos.
for n in range(2, 100):   # rango de numeros a comprobar si son primos.
   for x in range(2, n): # segundo bucle que comprobara si el numero es primo.
        if n % x == 0:   # modulo para comprobar si solo es divisible entre si.
           print(n, 'equals', x, '*', n//x) # demostración de que NO ES primo.
           break
   else:
       print(n, 'is a prime number') # al no encontrar un factor, es un numero primo.


