# 10102
v = int(input())
lst = list(input())

cnt_a = 0
cnt_b = 0

for i in lst:
    if i == "A" :
        cnt_a += 1
    elif i == "B" :
        cnt_b += 1

if cnt_a > cnt_b :
    print("A")
elif cnt_a < cnt_b :
    print("B")
else :
    print("Tie")