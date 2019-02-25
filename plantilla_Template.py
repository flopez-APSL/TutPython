from string import Template


t = Template('${tipo} de ${metros}, se vende por ${precio}. Causa: $causa.')
t = t.substitute(tipo='Piso', metros='125 m', precio='320.000 €', causa='Disputa Familiar')

print(t)

# lanza un error KeyError si algún item no es completado.
# t = Template('Return the $item to $owner.')
# d = dict(item='unladen swallow')
# t.substitute(d)
# t.safe_substitute(d)


# ejemplo para renombrar imágenes.
import time, os.path

photofiles = ['luna.jpeg', 'paisaje.jpg', 'catarata.jpeg']

class BatchRename(Template):
    delimiter = '%'


fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ') # recoje datos.


t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename) # ¿Por qué fragmenta la ruta?
    newname = t.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))

