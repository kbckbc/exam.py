def division(x,y):
    if int(y) == 0:
        res = '불능'
    else:
        res = int(x) / int(y)

    return res

def end_check(x,y):
    if x.isnumeric() and y.isnumeric():
        return False
    else:
        return True

while True:
    a = input('\n숫자1 입력:')
    b = input('숫자2 입력:')

    if end_check(a,b):
        print("\n 프로그램을 종료")
        break

    k=division(a,b)
    print("{} 나누기 {} 는 {} 입니다".format(a,b,k))


