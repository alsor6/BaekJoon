#25304
X = int(input())
N = int(input())

total_lst = []

for i in range(N) :
    a, b = map(int, input().split())
    total_lst.append(a*b)
    
if sum(total_lst) == X :
    print("Yes")
else :
    print("No")