#loops con dicionarrios
reyes = {'Felipe I': 'El Hermoso', 'Alfonso X': 'El Sabio', 'Felipe IV': 'El Grande'}

# la función items devuelve una tupla con la clave:valor del diccionario.
for k, v in reyes.items():
    print(k, v)

disparos = [' bang', ' bang', ' bang', ' bang']

for i, v in enumerate(disparos):
    print('le disparo, ', i+1, v,)


questions = ['name', 'Goal', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

#cuenta atrás..
for i in reversed(range(0, 11, 2)):
    print(i)

print('--------------------COMPARACIONES BOOLEANAS---------------------------------')
var1 = (1, 2, 3) < (1, 2, 4)
var2 = [1, 2, 3] < [1, 2, 4]
var3 = 'ABC' < 'C' < 'Pascal' < 'Python'
var4 =(1, 2, 3, 4) < (1, 2, 4)
var5 = (1, 2) < (1, 2, -1)
var6 = (1, 2, 3) == (1.0, 2.0, 3.0)
var7 = (1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4)

print(var1,
      var2,
      var3,
      var4,
      var5,
      var6,
      var7)
