print("* 딕셔너리: Hash 자료구조")
print("딕셔너리 형태: {키1:값1, 키2:값2}")
print("주의사항: 키와 값에 웬만한 자료구조가 다 올수 있고 섞어쓸 수 있음. ")
print('단, key는 리스트와 딕서녀리 못 씀. 키는 변경 불가능이어야 함')
print()

print("빈 딕셔너리 생성:", "x = {} or y = dict()")
a = {'health':490, 'mana':330, 'armor':18.72}; print(a)
print("a['health']:", a['health'])
print("딕셔너리 길이: len(" + str(a) + ")", len(a))
print("딕셔너리 값 확인: 'health' in a:", 'health' in a)
print("딕셔너리 값 확인: 'health' not in a:", 'health' not in a)
print()


my_dict = {'한국':60, '일본':40, '중국':50}

print("my_dict :", my_dict)
print("my_dict['한국']:", my_dict["한국"])
print("after my_dict['베트남'] = 30"); my_dict['베트남'] = 30; print("my_dict :", my_dict)
print("after my_dict['한국'] = 70"); my_dict['한국'] = 70; print('my_dict :', my_dict)
print()
print()

print('다음과 같이 순환조회 가능')
print('my_dict.items(): ', end='')
for k, v in my_dict.items():
    print("{0}:{1} ".format(k, v), end='')
print()

print('my_dict.values(): ', end='')
for v in my_dict.values():
    print(v, end = ',')
print()

print('my_dict.keys(): ', end='')
for k in my_dict.keys():
    print(k, end = ',')
print()

print()
print()

print('키워드 분석')
s = 'a,b,c,d,e,f,a,s,d,h,y,u,g,d,e,h,d,x,f,w,g,u,w,u'
s = s.split(',')
count1= {} # 결과 저장할 dict 정의
count2= dict() # 결과 저장할 dict 정의

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
