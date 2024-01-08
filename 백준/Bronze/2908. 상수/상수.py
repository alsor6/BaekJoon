# 2908
## 1
A, B = map(str, input().split())
new_A = ''
for i in A :
    new_A = i + new_A

new_B = ''
for i in B :
    new_B = i + new_B 

print(max(new_A, new_B))
