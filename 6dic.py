from warnings import catch_warnings


print("+ 딕셔너리: {키1:값1, 키2:값2} 자료형, Java 의 Map과 동일")
print("  - 주의사항: 키와 값에 웬만한 자료구조가 다 올수 있고 섞어쓸 수 있음. ")
print('  - 단, key는 리스트와 딕서녀리 못 씀. 키는 변경 불가능이어야 함')
print()

print("+ 빈 딕셔너리 생성:", "x = {} or y = dict()")
a = {'health':490, 'mana':330, 'armor':18.72}; print(a)
print("a['health']:", a['health'])
print("딕셔너리 길이: len(" + str(a) + ")", len(a))
print("딕셔너리 값 확인: 'health' in a:", 'health' in a)
print("딕셔너리 값 확인: 'health' not in a:", 'health' not in a)
print()


print('* dic for문')
my_dict = {'한국':60, '일본':40, '중국':50}
print("my_dict :", my_dict)
print()

if "없음" in my_dict:
    print('Finding key for 없음:', 'Yes')
else:
    print('Finding key for 없음:', 'No')

print("my_dict['한국']:", my_dict["한국"])
print()
print("after my_dict['베트남'] = 30"); my_dict['베트남'] = 30; print("my_dict :", my_dict)
print()
print("after my_dict['한국'] = 70"); my_dict['한국'] = 70; print('my_dict :', my_dict)
print()
print()

print('+ 딕셔너리 생성하는 여러 case')
print('  - 아래 케이스는 모두 다른 형태지만 결과물은 같다.')

print("JSON 형태 - dic = {'a':1,'b':2,'c':3}")
dic = {'a':1,'b':2,'c':3}
print('결과dic', dic, end='\n\n')


print("dict() 기본형 - dic = dict(a=1, b=2, c=3)")
print('키값을보면 따옴표가 없지만 딕셔너리로 만들고 나면 문자열로 바뀜')
dic = dict(a=1, b=2, c=3)
print('결과dic', dic, end='\n\n')

print("dict() & JSON 조합 형태 - dic = dict({'a':1,'b':2,'c':3})")
dic = dict({'a':1,'b':2,'c':3})
print('결과dic', dic, end='\n\n')

print("dict() & zip & list 조합 형태 - dic = dict(zip(['a','b','c'], [1,2,3]))")
dic = dict(zip(['a','b','c'], [1,2,3]))
print('결과dic', dic, end='\n\n')

print("dict() & list & tuple 조합 형태 - dic = dict([('a',1), ('b',2), ('c',3)])")
dic = dict([('a',1), ('b',2), ('c',3)])
print('결과dic', dic, end='\n\n')