N, X = map(int, input().split())
A = list(map(int, input().split()))
result = []
for i in range(len(A)):
    if A[i] < X:
        print(A[i], end = " ")
