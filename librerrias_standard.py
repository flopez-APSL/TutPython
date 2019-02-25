import os
directory = os.getcwd()      # Return the current working directory
print(directory)
# os.chdir('/server/accesslogs')   # Change current working directory
# os.system('mkdir creado_desde_Pycharm')   # Run the command mkdir in the system shell

# dir(os) returns a list of all module functions>

# help(os) returns an extensive manual page created from the module's docstrings>


import glob # uso de comodines para búsqueda de archivos.
archivos_py = glob.glob('*.py')
print(archivos_py)

import re # expresiones regulares.

expresion = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')

expresion2 = re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')

print(expresion, expresion2)

