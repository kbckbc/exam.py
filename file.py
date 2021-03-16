import sys

i = 0
for arg in sys.argv:
    print('arg[{0}] : [{1}]'.format(i,arg))
    i += 1

i = 0
for arg in sys.argv:
    if i != 0 :
        fileName = sys.argv[i]

        with open(fileName, 'rt', encoding='UTF8') as file:
            print('\nfileName [{0}]'.format(fileName))
            line = None
            j = 0
            while line != '':
                line = file.readline()
                print('%4d :%s' % (j, line.strip('\n')))
                j += 1
    i += 1
