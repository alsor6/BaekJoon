# 10886
n = int(input())
cute_cnt = 0
cute_not_cnt = 0
for i in range(n):
    a = int(input())
    if a == 1 :
        cute_cnt += 1
    elif a == 0 :
        cute_not_cnt += 1

if cute_cnt > cute_not_cnt :
    print("Junhee is cute!")
elif  cute_cnt < cute_not_cnt :
    print("Junhee is not cute!")