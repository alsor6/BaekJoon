# 2530
A, B, C = map(int, input().split())
time = int(input())

h = time//3600
m = (time%3600)//60
s = (time%3600)%60

A = A + h
B = B + m
C = C + s

if C >= 60 : 
    B = B+(C//60)
    C = C%60
if B >= 60 :
    A = A+(B//60)
    B = B%60
if A >= 24 :
    A = A%24
print(A, B, C)

