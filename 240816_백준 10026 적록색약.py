import sys
# 재귀함수 깊이 설정
sys.setrecursionlimit(1000000)

N = int(sys.stdin.readline())
rgb = [input() for _ in range(N)]
xb = [(c.replace('R','X')).replace('G','X') for c in rgb] # 'R','G'를 'X'로 변환

# 탐색여부 확인용 배열
f_rgb = [[0]*N for _ in range(N)]
f_xb = [[0]*N for _ in range(N)]


def find_area(N, col, f_col, c=None, a=None, b=None):
    # 탐색할 문자와 시작할 곳 찾기
    if c == None:
        for y in range(N):
            for x in range(N):
                if f_col[y][x] == 0:
                    f_col[y][x] = 1
                    c = col[y][x]
                    break
            if c != None: break
        if c == None:
            return False
    # 탐색할 문자가 정해져있다면 직전 좌표 받아오기
    else:
        x, y = a, b
    
    # '상' 탐색
    if y > 0:
        if (col[y-1][x] == c) and (f_col[y-1][x] == 0):
            f_col[y-1][x] = 1
            find_area(N, col, f_col, c=c, a=x, b=y-1)
    # '하' 탐색
    if y < N-1:
        if (col[y+1][x] == c) and (f_col[y+1][x] == 0):
            f_col[y+1][x] = 1
            find_area(N, col, f_col, c=c, a=x, b=y+1)
    # '좌' 탐색
    if x > 0:
        if (col[y][x-1] == c) and (f_col[y][x-1] == 0):
            f_col[y][x-1] = 1
            find_area(N, col, f_col, c=c, a=x-1, b=y)
    # '우' 탐색
    if x < N-1:
        if (col[y][x+1] == c) and (f_col[y][x+1] == 0):
            f_col[y][x+1] = 1
            find_area(N, col, f_col, c=c, a=x+1, b=y)
    
    return True



r = True; rgb_count = 0
while r:
    r = find_area(N, rgb, f_rgb)
    if r: rgb_count += 1

r = True; xb_count = 0
while r:
    r = find_area(N, xb, f_xb)
    if r: xb_count += 1

print(rgb_count, xb_count)
        



    
