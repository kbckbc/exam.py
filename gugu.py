print('Gugu ver 1.0\n')

while True :
    print('Which gugu? If you want to quit, put 0 :',end=' ') 
    
    dan = int(input())
    if dan == 0 :
        break;
    for j in range(9) :
        print("{0:2d} * {1:2d} = {2:2d}".format(dan,j+1,dan*(j+1)))
    print()# 한줄뛰우기
