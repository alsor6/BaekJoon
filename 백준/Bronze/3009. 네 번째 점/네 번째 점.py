# 3009
x_lst = []
y_lst = []
for i in range(3) :
    x, y = map(int, input().split())
    x_lst.append(x)
    y_lst.append(y)

answer_lst = []

if x_lst[0] == x_lst[1] :
    answer_lst.append(x_lst[2])
elif x_lst[0] == x_lst[2] :
    answer_lst.append(x_lst[1])
elif x_lst[1] == x_lst[2] :
    answer_lst.append(x_lst[0])
    
if y_lst[0] == y_lst[1] :
    answer_lst.append(y_lst[2])
elif y_lst[0] == y_lst[2] :
    answer_lst.append(y_lst[1])
elif y_lst[1] == y_lst[2] :
    answer_lst.append(y_lst[0])

for i in answer_lst :
    print(i, end = ' ')