# import sys
# n = int(sys.stdin.readline())
# st = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# st.sort(key=lambda x:x[0]) # 시작 시간 순서대로 정렬

# ans = 0
# while len(st) != 0:
#     ans += 1
#     if len(st) != 0:
#         f = st[0]
#         del st[0]
#         st_ex= []
#         for i in range(len(st)):
#             if  f[1] <= st[i][0]:
#                 f = st[i]
#             else:
#                 st_ex.append(st[i])
#         st = st_ex

# print(ans)


import heapq 
# 입력 처리
n = int(input())
st = [tuple(map(int, input().split())) for _ in range(n)]

# 수업을 시작 시간 순으로 정렬
st.sort()

# 힙 초기화
heap = []

# 수업 순회
for s, t in st:
    # 힙이 비어있지 않고, 현재 수업의 시작 시간이 가장 먼저 끝나는 수업의 끝나는 시간 이후라면
    if heap and heap[0] <= s:
        heapq.heappop(heap)  # 끝난 수업의 강의실을 재사용
    heapq.heappush(heap, t)  # 현재 수업의 끝나는 시간을 힙에 추가
    print('s:', s,'t :', t, 'heap :', heap)

print(len(heap))