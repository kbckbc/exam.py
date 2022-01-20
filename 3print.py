import string

print("* 출력하기: print")
print("쉼표로 구분하면 한칸 공백으로 분리 출력: print(1,2,3)", end=' '); print(1,2,3)
print("sep로 구분자 변경 가능: print(1,2,3,sep='.')", end=' '); print(1,2,3,sep='.')
print("end로 라인피드 변경 가능: print(1,2,3,end='')", end=''); print("이렇게 하면", end=''); print("라인피드 없이 출력이 끝남")
print()

# 정렬
print("포매팅: format 함수 사용하기")
s9 = 'this is {0:<10} | done {1:<5} |'.format('left', 'a'); print(s9)
s12 = 'this is {0:-<10} | done {1:o<5} |'.format('left', 'a'); print(s12)
s10 = 'this is {0:>10} | done {1:>5} |'.format('right', 'b'); print(s10)
s13 = 'this is {0:+>10} | done {1:0>5} |'.format('right', 'b'); print(s13)
s11 = 'this is {0:^10} | done {1:^5} |'.format('center', 'c'); print(s11)
s14 = 'this is {0:.^10} | done {1:@^5} |'.format('center', 'c'); print(s14)
print()

print("포매팅: % 사용하기")
print("%d + %d = %d" % (1,2,3)) 
print("Name: %s, Age: %d" % ("Kevin", 17))



print("replace():", "'Hello, world!'.replace('world','Python'):", 'Hello, world!'.replace('world','Python'))
print("split():", "'apple pear orange'.split():", 'apple pear orange'.split())
print("join():", "'-'.join(['apple', 'pear', 'orange']):", '-'.join(['apple', 'pear', 'orange']))
print("upper() lower():", "'python'.upper()':", 'python'.upper())
print("lstrip():", "'   python   '.lstrip()':", '   python   '.lstrip())
print("strip():", "'   python   '.strip()':", '   python   '.strip())
print("strip(string.punctutation):", "',.   python  ., '.strip(string.punctuation)+' '':", ',.   python  ., '.strip(string.punctuation + ' '))
print("ljust():", "'python'.ljust(10)':", 'python'.ljust(10))
print("rjust():", "'python'.rjust(10)':", 'python'.rjust(10))
print("center():", "'python'.center(10)':", 'python'.center(10))
print("find():", "'apple pineapple'.find('pl'):", 'apple pineapple'.find('pl'))
print("find():", "'apple pineapple'.find('xy'):", 'apple pineapple'.find('xy'))
print("index():", "'apple pineapple'.index('pl'):", 'apple pineapple'.index('pl'))
print("count():", "'apple pineapple'.count('pl'):", 'apple pineapple'.count('pl'))


