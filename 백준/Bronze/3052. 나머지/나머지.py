num_lst = []
spare_lst = []
for _ in range(10):
    N = int(input())
    num_lst.append(N)

for i in range(len(num_lst)):
    spare = num_lst[i]%42
    spare_lst.append(spare)

result = set(spare_lst)
print(len(result))