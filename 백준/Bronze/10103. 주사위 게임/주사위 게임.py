# 10103
N = int(input())
C_score, S_score = 100, 100

for i in range(N):
    C, S = map(int, input().split())
    if C < S :
        C_score -= S
    elif C > S :
        S_score -= C
print(C_score)
print(S_score)    
