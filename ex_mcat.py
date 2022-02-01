# ex_mcat
# Author : Byeongchan Gwak, kbckbc@gamil.comk, b.gwak@wustl.edu
# This is a immitation program of cat command in Unix
# Usage : ex_mcat -n file file file..
# Option 
#    -n : Number all output lines

import sys

debug = False;

def Usage():
    print('Usage : mcat [OPTION] ... [FILE]')
    print('    -n,-N : Number all output lines ')


if debug == True:
    print('len(sys.argv)', len(sys.argv))
    i = 0
    for arg in sys.argv:
        print('arg[{}] : [{}]'.format(i,arg))
        i += 1


if len(sys.argv) == 1:
    Usage()
    exit()


optionN = False
startArgv = 1


option = sys.argv[1]
if len(option) == 2 and option[0] == '-':
    if option[1].upper() == 'N':
        optionN = True
        startArgv = 2
    else:
        Usage()
        exit()

    
for i in range(startArgv,len(sys.argv)):
    fileName = sys.argv[i]

    with open(fileName, 'rt', encoding='UTF8') as file:
        print('\n!!! Start of a file [{0}]'.format(fileName))
        line = None
        j = 1
        while line != '':
            line = file.readline()
            if optionN == True:
                print('%4d :%s' % (j, line.strip('\n')))
            else :
                print('%s' % (line.strip('\n')))
            j += 1
