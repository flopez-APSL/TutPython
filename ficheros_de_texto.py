#f = open('textfile.txt', 'r+') # r+ lee y escribe.

with open('textfile.txt') as f:
    read_data = f.read()
    print(read_data)
    f.closed

with open('textfile.txt') as f:
    read_data = f.readline()
    print(read_data)
    f.closed

print('------------------------------------------------------------------')

with open('textfile.txt', 'a') as f:
    f.write(' Esto, está demás... ') # para escribir al final.. ..sin borrar.
    f.closed


with open('textfile.txt') as f:
    read_data = f.readline()
    print(read_data)


with open('textfile.txt') as f:
    for line in f:
        print(line, end='')
        f.closed

