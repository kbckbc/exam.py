print("* 출력하기: print")
print("쉼표로 구분하면 한칸 공백으로 분리 출력: print(1,2,3)", end=' '); print(1,2,3)
print("sep로 구분자 변경 가능: print(1,2,3,sep='.')", end=' '); print(1,2,3,sep='.')
print("end로 라인피드 변경 가능: print(1,2,3,end='')", end=''); print("이렇게 하면", end=''); print("라인피드 없이 출력이 끝남")
print()

# 왼쪽 정렬
# 오른쪽 정렬
# 가운데 정렬
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
