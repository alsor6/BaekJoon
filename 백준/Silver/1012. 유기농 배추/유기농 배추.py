import sys
sys.setrecursionlimit(10**6)
#변수 받기
T = int(input())


#함수부
def bfs(y,x):
    if y < 0 or y >= N or x <0 or x >= M:
        return False
    if ground[y][x] == 1:
        ground[y][x] = 0
        bfs(y-1, x)
        bfs(y, x-1)
        bfs(y+1, x)
        bfs(y, x+1)
        return True
    return False


#결과 실행
for _ in range(T):
    #ground 생성 및 배추 심기
    M, N, K = map(int, input().split())
    ground = [[0 for _ in range(M)]for _ in range(N)]
    for _ in range(K) :
        x, y = map(int, input().split())
        ground[y][x] = 1

    #지렁이 수 세기
    count = 0
    for i in range(N):
        for j in range(M):
            if bfs(i,j) == True :
                count += 1
    print(count)
