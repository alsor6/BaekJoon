# 2476
n = int(input())
prize = 0
challenger = []
for i in range(n):
    n1, n2, n3 = map(int, input().split())
    if n1 == n2 == n3 :
        prize = 10000 + n1*1000
    elif n1 == n2 and n2 != n3 :
        prize = 1000 + n1*100
    elif n2 == n3 and n3 != n1 :
        prize = 1000 + n2*100
    elif n3 == n1 and n1 != n2 :
        prize = 1000 + n3*100
    else : 
        prize = max(n1,n2,n3)*100
    challenger.append(prize)
print(max(challenger))
        