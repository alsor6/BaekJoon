# 10988
s = list(input())
s_lst = []
for i in range(len(s)) :
    if s[i] == s[-(i+1)] :
        s_lst.append(0)
    else :
        s_lst.append(1)
if sum(s_lst) == 0 :
    print(1)
else : 
    print(0)
