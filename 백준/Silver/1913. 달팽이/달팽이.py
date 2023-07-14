dx = [0,1,0,-1]
dy = [1,0,-1,0]
d = 0
x,y = 0, 0
n = int(input())
N = int(input())
n2 = n*n
A = [[0 for _ in range(n)] for _ in range(n)]
while n2 > 0 : 
    A[y][x] = n2
    if y+dy[d] >= n or x+dx[d] >= n or y+dy[d] < 0 or x+dx[d] < 0 or A[y+dy[d]][x+dx[d]] != 0 :
        d = (d+1)%4
    x = x + dx[d]
    y = y + dy[d]
    n2 -= 1

N_lst = []    
for i in range(n):
    for k in range(n):
        print(A[i][k], end=' ')
        if A[i][k] == N :
            N_lst.append(i+1)
            N_lst.append(k+1)
    print()
print(N_lst[0],N_lst[1])
