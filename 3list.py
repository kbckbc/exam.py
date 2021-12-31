import copy
print("+ About List")
print("빈 리스트 생성:", "a = [] or b = list()")
print("리스트 값은 타입이 달라도 가능:", "\n\tperson=['james',17,175.3,True]", ['james',17,175.3,True])
print("튜플은 읽기 전용 리스트라고 생각하면 됨, 괄호모양이 다름: a = (1,2,3,4,5)","\n\t", (1,2,3,4,5))
print()
print()

print('extend는 리스트끝에 리스트를 연결하여 확장')
print('append는 리스트끝에 요소 하나를 추가함')
print('insert는 원하는 지점에서 요소를 추가할 수 있음')
print('pop은 마지막 혹은 원하는 지점의 요소를 꺼내서 삭제')
print()
print()

a = [10,20,30]
print("a:",a); print("a len(a):",len(a))
a.extend([1000]); print("a extend [1000]:",a)
a.append(500); print("a append 500:",a)
a.append([500]); print("a append [500]:",a)
a.insert(2,800); print("a insert 2 800:",a)
a.insert(2,[700]); print("a insert 2 [700]:",a)
print("a pop():",a.pop()); print("a after pop():",a)
print("a pop(1):",a.pop(1)); print("a after pop(1):",a)
print()
print()

print('reverse는 list 순서 뒤집기. 역정렬아님')
print('sort는 list 정렬')
print('index는 list 안에서 인덱스 순서를 찾아줌')
print('마지막 요소에 접근은 -1 활용. 쓰기전에 list 있는지 부터 체크')
print('min, max, sum 함수 사용 가능. list 메쏘드 아님주의!')
print('del은 list 원하는곳 지우기. del 은 list 메쏘드 아님 주의!')
print('clear는 list 지우기')
print()
print()

b = [3,2,4,1,5]
print("b:",b)
b.reverse(); print("after b.reverse:",b)
b.sort(); print("after b.sort:",b)
if not b: print("b 리스트 비었음")
elif b: print("b 리스트 들어있음")
# 리스트가 있는지 체크하고 -1 써야함
if b: print("b b[-1]:",b[-1])

try:
    print("b index(1):",b.index(1))
    print("b index(5):",b.index(5))
    print("b index(6):",b.index(6))
except Exception as inst:
    print('>> Unexpected Exception <<')
    print(type(inst))
    print(inst)

print("b min{0}, max{1}, sum{2}:", min(b), max(b), sum(b))
del b[1:2]; print("after del b[1:2]:",b)
b.clear(); print("after b.clear():",b)
print()
print()

print("+ 리스트 반복문")
a = ["a","b","c","d","e"]
for i in a:
    print(i, end=' ')
print()
for i, v in enumerate(a):
    print(i, v, end=',')
print()
print()
print()


print("+ 리스트 할당 복사")
a = [1,2,3]; b = [10,20,30]; b.append(a)
print("a:", a, "b:", b)

c = b.copy(); 
print("before chage value in a: c = b.copy():", c)
a[0] = a[0]*100
print("after chage value in a: c = b.copy():", c)

a = [1,2,3]; b = [10,20,30]; b.append(a)
c = copy.deepcopy(b) 
print("before chage value in a: c = copy.deepcopy(b):", c)
a[0] = a[0]*100
print("after chage value in a: c = copy.deepcopy(b):", c)
print()
print()

print('+ List comprehension')
print('리스트 안에 식, for문, if문을 사용하여 리스트를 생성하는 개념')

print('a = [i for i in range(10)]')
print('a :', [i for i in range(10)])

print('a = [i for i in range(10)]')
print('odd :', [i for i in range(10) if i%2 == 1])
print('even :', [i for i in range(10) if i%2 == 0])

print('a = [i * 2 for i in range(10)]')
print('a :', [i*2 for i in range(10)])

print('a = [i * 5 for i in range(10) if i % 2 == 1]')
print('a :', [i * 5 for i in range(10) if i % 2 == 1])

print('a = [i * j for j in range(2,10) for i in range(1,10)]')
print('a :', [i * j for j in range(2,10) for i in range(1,10)])
print()