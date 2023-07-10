N, M = map(int, input().split())
org_lst = []
for k in range(1,N+1):
    org_lst.append(k)
for _ in range(1,M+1):
    i, j = list(map(int, input().split()))
    org_lst[i-1], org_lst[j-1] = org_lst[j-1], org_lst[i-1]
for k in range(len(org_lst)):
    print(org_lst[k], end=' ')