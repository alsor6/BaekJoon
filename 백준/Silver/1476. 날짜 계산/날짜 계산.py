E, S, M = map(int, input().split())
e = 0
s = 0
m = 0
total = 0
while True : 
    e += 1
    s += 1
    m += 1
    total += 1
    if e > 15 :
        e = 1
    if s > 28 :
        s = 1
    if m > 19 :
        m = 1
    if e == E and s == S and m ==M:
        print(total)
        break