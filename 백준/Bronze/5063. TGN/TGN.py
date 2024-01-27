# 5063
n = int(input())
for i in range(n):
    r, e, c = map(int, input().split())
    ad =  e - c     
    if r < ad :
        print("advertise")
    elif r > ad :
        print("do not advertise")
    elif r == ad :
        print("does not matter")