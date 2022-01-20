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