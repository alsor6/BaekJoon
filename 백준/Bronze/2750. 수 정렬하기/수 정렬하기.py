N = int(input())
lst =[]
for i in range(N):
    num = int(input())
    lst.append(num)
lst.sort()
for i in range(len(lst)):
    print(lst[i])