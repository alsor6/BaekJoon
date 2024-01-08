## 3
A, B = map(str, input().split())
new_A = A[::-1]
new_B = B[::-1]

print(max(new_A, new_B))