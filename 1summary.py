print("* 일반적사항")
print("세미콜론 없고, 들여쓰기 자체가 문법임")
print("나눗셈의 결과는 무조건 실수:","4/2 =", 5/2)
print("거듭제곱 연산자는 **:", "2**10 =", 2**10)
print("type 알아내기:", "type(10)", type(10))
print("변수 swap하기: x,y = y,x")
print("== != 는 value 비교, is, is not 은 객체를 비교:")
# print("\t1==1.0", 1==1.0, "1 is 1.0", 1 is 1.0)
print("range(10)은", range(10), "이고 range(0, 10)은 0에서 부터 9까지 숫자 생성")
print("range(0,10,2)은 0 부터 9까지 2씩 증가하여 생성:", list(range(0,10,2)))
print()


print("* 입력받기: input")
print("입력받기: x = input('문자열 입력하세요')")
print("입력받기: a, b = input('문자열 두 개 입력하세요').split()")
print("입력받기: a, b = map(int, input('문자열 두 개 입력하세요').split())")
print()




print("* 시퀀스 자료형: list, tuple, range, str")
print("tuple, range, str 은 읽기 전용 시퀀스임. del 못 씀")
print("특정 값 확인: 30 in [0,10,20,30]:", 30 in [0,10,20,30])
print("특정 값 확인: 30 not in [0,10,20,30]:", 30 not in [0,10,20,30])
print("시퀀스 연결: [0,10,20] + [30,40,50]", [0,10,20] + [30,40,50])
print("시퀀스 연결: 문자랑 숫자랑 연결하려면 type casting 필요 '1 + 2 = ' + str(3) =>", "1 + 2 = " + str(3))
print("시퀀스 요소 길이: len([1,2,3,4,5])", len([1,2,3,4,5]))
print("시퀀스 요소 접근: s='ABCDE', s[3]", "ABCDE"[3])
print("시퀀스 요소 첫번째 접근: s='ABCDE', s[0]", "ABCDE"[0])
print("시퀀스 요소 마지막 접근: s='ABCDE', s[-1]", "ABCDE"[-1])
print("시퀀스 요소 삭제: del 시퀀스객체[인덱스]")
print()


print("* 시퀀스 슬라이스")
print("시퀀스객체[시작인덱스:끝인덱스:증가폭]")
print("a=[0,1,2,3,4]을 [0:2] 하면 0,1 을 슬라이스 함. 끝 인덱스는 미포함", [0,1,2,3,4][0:2])
print("a[::] 는 전체 리스트를 가지고 옴", [0,1,2,3,4][::])
print("a[::2] 는 전체 리스트 대상으로 2씩 증가하며 가져옴", [0,1,2,3,4][::2])
print("a[::-1] 는 전체 리스트 역순으로 가져옴", [0,1,2,3,4][::-1])
print()


print("* 리스트")
print("빈 리스트 생성:", "a = [] or b = list()")
print("리스트 값은 타입이 달라도 가능:", "person=['james',17,175.3,True]", ['james',17,175.3,True])
print("튜플은 읽기 전용 리스트라고 생각하면 됨, 괄호모양이 다름: a = (1,2,3,4,5)",(1,2,3,4,5))
a = print("")
print()


print("* 딕셔너리: Hash 자료구조")
print("빈 딕셔너리 생성:", "x = {} or y = dict()")
print("딕셔너리 형태: {키1:값1, 키2:값2}")
print("주의사항: 키와 값에 웬만한 자료구조가 다 올수 있고 섞어쓸 수 있음. 단 키에는 리스트와 딕서녀리 못 씀")
a = {'health':490, 'mana':330, 'armor':18.72}; print(a)
print("a['health']:", a['health'])
print("딕셔너리 길이: len(" + str(a) + ")", len(a))
print("딕셔너리 값 확인: 'health' in a:", 'health' in a)
print("딕셔너리 값 확인: 'health' not in a:", 'health' not in a)
print()

