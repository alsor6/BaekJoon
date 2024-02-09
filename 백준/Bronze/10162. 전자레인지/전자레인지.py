# 10162
n = int(input())

A = n//300
B = (n%300)//60
C = (n%60)//10
D = n%10

if D == 0 :
    print(A, B, C)
else :
    print(-1)
    