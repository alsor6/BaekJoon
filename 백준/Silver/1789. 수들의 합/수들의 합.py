s = int(input())
cnt = 0
sum_i = 0
for i in range(1, s+1):
    sum_i += i
    cnt += 1
    if sum_i > s:
        break
if s > 1 :
    cnt -= 1
    print(cnt)
elif s == 1 :
    print(cnt)