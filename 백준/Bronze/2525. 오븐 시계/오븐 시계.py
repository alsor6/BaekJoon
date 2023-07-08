A, B = map(int, input().split())
C = int(input())
h = C//60
m = C%60
if B+m >= 60 :
    H = A+h+1
    M = (B+m)%60
    if H >= 24:
        if H == 24:
            H = 0
        else :
            H = H%24
elif B+m <60 :
    H = A+h
    M = B+m
    if H >= 24:
        if H == 24:
            H = 0
        else :
            H = H%24
print(H, M)