N, M = map(int, input().split())
lst = [0 for n in range(N)] 
for _ in range(M):
    i, j, k = list(map(int, input().split()))
    for z in range(i-1,j):
        lst[z] = k
for z in range(len(lst)):
    print(lst[z], end=" ")