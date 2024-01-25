# 2935
lst = []
for i in range(3):
    word = input()
    lst.append(word)

if lst[1] == "+":
    print(int(lst[0]) + int(lst[2]))
if lst[1] == "*":
    print(int(lst[0]) * int(lst[2]))
