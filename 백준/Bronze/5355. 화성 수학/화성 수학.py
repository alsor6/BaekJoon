# 5355
n = int(input())
for i in range(n):
    lst = list(map(str, input().split()))
    result = 0
    for i in lst :
        if i == '@' :
            result *= 3
        elif i == '%' :
            result += 5
        elif i == '#' :
            result -= 7
        else :
            result += float(i)
    print('%.2f'%result)