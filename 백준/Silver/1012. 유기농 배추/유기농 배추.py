import sys
sys.setrecursionlimit(100000)
def dfs(y,x):
    if x < 0 or x >= m or y < 0 or y >= n:
        return False
    if ground[y][x] == 1:
        ground[y][x] = 0
        dfs(y-1, x)
        dfs(y, x-1)
        dfs(y+1, x)
        dfs(y, x+1)
        return True
    return False

#test case
t = int(input())

#ground 생성
for _ in range(t):
    m,n,k = list(map(int, input().split()))
    # 모두 0인 ground 생성
    ground = [[0 for _ in range(m)] for _ in range(n)]
    # 배추 심어진 곳에 1 표기
    for _ in range(k):
        m1, n1 = map(int, input().split())
        ground[n1][m1] = 1

    count = 0
    for i in range(n):
        for j in range(m):
            if dfs(i,j) == True :
                count += 1
    print(count)