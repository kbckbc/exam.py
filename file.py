import sys

i = 0
for arg in sys.argv:
    print('arg[{0}] : [{1}]'.format(i,arg))
    i += 1

fileName = sys.argv[1]

with open(fileName, 'rt', encoding='UTF8') as file:
    line = None
    i = 0
    while line != '':
        line = file.readline()
        print('{0} : {1}'.format(i,line.strip('\n')))
        i += 1
