import json

jdocument = json.dumps([1, 'simple', 'list'])

print(jdocument)

diccionario = {'Matias':'Prats',
               'Luis':'Amstrong',
               'Samel':'L. Jackson',
               }
textfile = open('Diccionario_a_JSON.txt', 'w')

jdocument = json.dump(diccionario, textfile)

print(jdocument)













# ¿Qué es esto?
# from io import StringIO
# io = StringIO()
# json.dump(['streaming API'], io)
# io.getvalue()