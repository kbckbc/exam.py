"""
+ list for 반복문
  for i in a: print(i, end=' ')
  for i, v in enumerate(a): print(i, v, end=',')
+ dic for문
  for k, v in my_dict.items(): print("{0}:{1} ".format(k, v), end='')
  for k in my_dict.keys(): print(k, end = ',')
  for v in my_dict.values(): print(v, end = ',')
"""

print("+ list for 반복문")
a = ["a","b","c","d","e"]
print('a:', a)
print()

for i in a: print(i, end=' ')
print()
for i, v in enumerate(a): print(i, v, end=',')
print()
print()
print()

print('+ dic for문')
my_dict = {'한국':60, '일본':40, '중국':50}
print('my_dict:', my_dict)
print()

print('my_dict.items(): ', end='')
for k, v in my_dict.items(): print("{0}:{1} ".format(k, v), end='')
print()

print('my_dict.keys(): ', end='')
for k in my_dict.keys(): print(k, end = ',')
print()

print('my_dict.values(): ', end='')
for v in my_dict.values(): print(v, end = ',')
print()
