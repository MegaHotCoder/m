#10815

import sys
from collections import deque

def list_int():
  x = sys.stdin.readline()
  x = x.split(" ")
  y = list(map(int, x))
  return y

def find(a, x, y):

    
    mid = a // 2  # 중간 인덱스 계산
    mid_val = x[mid]  # 중간 값

    if mid_val == y:
        return 1  # 값을 찾음
    elif mid_val > y:
        if mid == 0:
            return 0
        else:        
            return find(mid, x[:mid], y)
    else:
        if mid == 0:
            return 0    
        else:
            return find(a - mid - 1, x[mid + 1:], y)
    
    
# 5
# 6 3 2 10 -10
# 8
# 10 9 -5 2 3 4 5 -10


n = int(sys.stdin.readline().strip())  # 공백 제거 후 정수 변환
n1 = list_int()
n1 = sorted(n1)
m = int(sys.stdin.readline().strip())
m1 = list_int()

for i in range(m):
  print(find(n,n1,m1[i]), end=" ")
    

