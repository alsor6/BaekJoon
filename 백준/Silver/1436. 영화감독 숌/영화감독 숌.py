N = int(input())
count = 0
a = 0
while True:
    a += 1
    if "666" in str(a):
        count += 1
    if count == N:
        break
print(a)