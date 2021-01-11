print('Which gugu ?',end=' ')

dan = int(input())
for j in range(9):
  print("{0:2d} * {1:2d} = {2:2d}".format(dan,j+1,dan*(j+1)))
