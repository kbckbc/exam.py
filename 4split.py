a='곽병찬,1,2|이연주,3,4|곽지성,5,6|곽채윤,7,8'

print('\n')
print('+ 원문 그대로')
print("  - a:{0}".format(a))

print()
print('+ b = a.split('|')')
b = a.split('|')
print("  - b:{0}".format(b))

print()
print('+ b split. 다른변수 대입')
c = list()
d = list()
for i in range(len(b)):
    c.append(b[i].split(','))
    d.extend(b[i].split(','))
print("  - b:{0}".format(b))
print("  - c.append(b[i].split(','):{0}".format(c))
print("  - d.extend(b[i].split(','):{0}".format(d))

print()
print('+ b 덮어쓰기 전 갯수')
print("  - b:{0}".format(b))
print('  - b    의 길이: {0}'.format(len(b)))
print('  - b[0] 의 길이: {0}'.format(len(b[0])))

print()
print('+ b split. 덮어쓰기')
for i in range(len(b)):
    b[i] = b[i].split(',')

print()
print('+ b 덮어쓰기 후 갯수')
print("  - b:{0}".format(b))
print('  - b    의 길이: {0}'.format(len(b)))
print('  - b[0] 의 길이: {0}'.format(len(b[0])))

