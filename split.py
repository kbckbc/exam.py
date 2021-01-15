a='곽병찬,1,2|이연주,3,4|곽지성,5,6|곽채윤,7,8'
print('\n원문 그대로')
print("a:{0}".format(a))

print('\n바깥쪽 리스트 split')
b = a.split('|')
print("b:{0}".format(b))

for i in range(len(b)):
    print("\nb[{0}]:{1}".format(i,b[i]))
    c = b[i].split(',')
    for j in range(len(c)):
        print("     c[{0}]:{1}".format(j,c[j]),end=' ')

print('\n변환전 갯수')
print(len(b))
print(len(b[0]))

print('\n안쪽 리스트 split')
for i in range(len(b)):
    print("b[{0}]:{1}".format(i,b[i]))
    b[i] = b[i].split(',')
    print("b[{0}]:{1}".format(i,b[i]))

print('\n변환후 갯수')
print(len(b))
print(len(b[0]))



