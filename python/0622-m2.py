# OX퀴즈
# "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.

# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.

# OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

import sys
n = int(input())
arr = list()

for i in range(n):
    arr.append(list(sys.stdin.readline().rstrip()))

for quiz in arr:
  gogo = 0
  result = 0
  for apb in quiz:
    if apb == "X":
      gogo = 0
    elif apb == "O":
      gogo += 1
    result += gogo
  print(result)