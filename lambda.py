# 람다 함수
# 이름없이 인수와 수식을 통해 값을 반환하는 함수
# lambda 인수: 반환할 식
k = lambda x,y: x*y
print('k = lambda x,y: x*y')
print('k(10,5):',k(10,5))


# 튜플 및 리스트도 반환 가능
p = lambda x,y: [x+y,x-y,x*y]
print('p = lambda x,y: [x+y,x-y,x*y]')
print('p(10,5):',p(10,5))

# 람다 함수를 리스트 값으로 가질수 있음
m = ['파이썬',lambda x: x*x, 100]
mp = ['파이썬','lambda x: x*x', 100]

print('m:',mp)
for i in range(len(m)):
    print('m[{}]:'.format(i),m[i])
print(m[1](5)) # 람다 함수 호출

# 람다 함수에 조건식도 쓸 수 있음
# 람다에 조건식을 썼다면 무조건 else 를 써야 함. elif 는 사용 못함
# map 함수 : 첫번째 인자에서 지정한 함수를 두번째 파람에 적용시킴
# return 값은 iterator 라서 list 롤 묶던지 해야함
# map(함수, 반복가능한객체)
a = [i for i in range(1,11)]
print('a :', a)
print(list(map(lambda x: str(x) if x % 3 == 0 else x, a)))

# filter 함수: 첫번째 인자에서 함수가 True 때 두번째 파람을 통과시킴
# return 값은 iterator 라서 list 롤 묶던지 해야함
# filter(함수, 반복가능한객체)
a = range(1,11)
print('a :', a)
a = list(filter(lambda x: x % 2 == 0, range(1,11)))
print('a :', a)

b = range(1,11)
print('b :', b)
b = list(filter(lambda x: x % 2 == 1, range(1,11)))
print('b :', b)


