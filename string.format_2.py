print('The story of {0}, {1}, and {other}.'.format('Me',
                                                   'You', other='Others'))

table = {'Fernando': 622646626,
         'Enrique ': 688987897,
         'Luisa': 673789291}

print('Fernando: {Fernando:d}; Enrique: {Enrique :d}; Luisa: {Luisa:d}'.format(**table))

for x in range(1, 11): print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
# Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))


