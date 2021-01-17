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

