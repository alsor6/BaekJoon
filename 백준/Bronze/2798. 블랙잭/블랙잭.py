N, M = map(int, input().split())
card = list(map(int, input().split()))

sum_list = []
for i in range(len(card)):
    for j in range(len(card)):
        for k in range(len(card)):
            if i != k and k != j and j != i:
                sum = card[i] + card[j] + card[k]
                if sum <= M:
                    sum_list.append(sum)
                
sum_set = set(sum_list)
sum_set_list = list(sum_set)

sub_list = []
for i in range(len(sum_set_list)):
    sub = M - sum_set_list[i]
    sub_list.append(sub)

idx = sub_list.index(min(sub_list))
print(sum_set_list[idx])