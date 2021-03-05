print('dic 는 키:값 자료 구조임')
print('키는 숫자 문자 모두 가능하나 변경 불가능이어야 함')
print()

my_dict = {'한국':60, '일본':40, '중국':50}
print('my_dict :', my_dict)
print("my_dict['한국']:", my_dict['한국'])

print('dic에 바로 추가 가능')
my_dict['베트남'] = 30
print('my_dict :', my_dict)

print('다음과 같이 순환조회 가능')
print('\nitems()')
for k, v in my_dict.items():
    print(k,v, end = ' ')
print()

print('\nvalues()')
for v in my_dict.values():
    print(v, end = ' ')
print()

print('\nkeys()')
for k in my_dict.keys():
    print(k, end = ' ')
print()


print('키워드 분석')
s = 'a,b,c,d,e,f,a,s,d,h,y,u,g,d,e,h,d,x,f,w,g,u,w,u'
s = s.split(',')
count1= {} # 결과 저장할 맵 정의
count2= {} # 결과 저장할 맵 정의

# 이런 형태로 카운팅도 되고
for k in s:
    if k in count1:
        count1[k] += 1
    else:
        count1[k] = 1
# 이런형태도 카운팅 된다
for k in s:
    count2.setdefault(k,0)
    count2[k] = count2[k] + 1

print('카운팅 결과 출력')
for key, value in count1.items():
    print('count1 : key[{0}], value[{1}]'.format(key, value))
for key, value in count2.items():
    print('count2 : key[{0}], value[{1}]'.format(key, value))
