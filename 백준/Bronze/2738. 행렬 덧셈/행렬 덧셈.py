A = []
B = []
N, M = map(int, input().split())
for i in range(N):
    a = list(map(int, input().split()))
    A.append(a)
for i in range(N):
    b = list(map(int, input().split()))
    B.append(b)
    
for i in range(N):
    for k in range(M):
        print(A[i][k] + B[i][k], end = " ")
    print()