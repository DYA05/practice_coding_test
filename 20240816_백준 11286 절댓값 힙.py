# 단순리스트론 시간초과
import sys
n = int(sys.stdin.readline())
x = [int(sys.stdin.readline()) for _ in range(n)]

arr = []
for n in x:
    if n != 0:
        arr.append(n)
    else:
        if len(arr) == 0:
            print(0)
        else:
            abs_arr = [abs(i) for i in arr]
            k = min(abs_arr)
            if -k in arr:
                print(-k)
                arr.remove(-k)
            else:
                print(k)
                arr.remove(k)