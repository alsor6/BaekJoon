#9095 1,2,3
dp_lst = []
def hap(x):
    if x == 1 :
        return 1
    elif x == 2 :
        return 2
    elif x == 3 :
        return 4
    return hap(x-1) + hap(x-2) + hap(x-3)

t = int(input())
for _ in range(t):
    x = int(input())
    print(hap(x))