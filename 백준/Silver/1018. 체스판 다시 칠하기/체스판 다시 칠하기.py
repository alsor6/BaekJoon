#0 체스판 크기 받기
n, m = map(int, input().split())
lst = []
#1 큰 체스판 만들기
large_lst = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    lst.append(input())

for i in range(n):
    for k in range(m):
        large_lst[i][k] = lst[i][k]
    #large_lst = list(map(str, input()))
draw1_lst = []
draw2_lst = []

#2 작은 체스판 만들기
for l in range(n-7):
    for l2 in range(m-7):
        draw1 = 0
        draw2 = 0
        for s1 in range(l, l+8):
            for s2 in range(l2, l2+8):
                if (s1+s2)%2 == 0:
                    if large_lst[s1][s2] != "W":
                        draw1 += 1
                if (s1+s2)%2 == 1:
                    if large_lst[s1][s2] != "B":
                        draw1 += 1
                if (s1+s2)%2 == 0:
                    if large_lst[s1][s2] != "B":
                        draw2 += 1
                if (s1+s2)%2 == 1:
                    if large_lst[s1][s2] != "W":
                        draw2 += 1
        draw1_lst.append(draw1)
        draw2_lst.append(draw2)
result_lst = draw1_lst + draw2_lst
print(min(result_lst))