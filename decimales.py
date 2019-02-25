#!/usr/bin/python3.7  # ésta era tu ruta. Pero no te funcionó.



# precision decimal para las operaciones que son necesarias.
from decimal import *
withdecimal = round(Decimal('0.70') * Decimal('1.05'), 2)

normal_operation = round(.70 * 1.05, 2)

print('con el módulo decimal: ',withdecimal,' Sin el módulo: ',normal_operation)


# imita las operaciones hechas a mano. evitando los problemas del flotante binario.

withdecimal = Decimal('1.00') % Decimal('.10')

normal_operation = 1.00 % 0.10
print('Con decimal: ',withdecimal, ' Sin el módulo: ',normal_operation)


withdecimal = sum([Decimal('0.1')]*10) == Decimal('1.0')

normal_operation = ([0.1]*10) == 1.

print('Con decimal: ',withdecimal, ' Sin el módulo: ',normal_operation)

