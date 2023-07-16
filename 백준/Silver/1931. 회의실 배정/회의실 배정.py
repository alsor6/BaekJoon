n = int(input())
lst_list = []
for i in range(n):
    lst = list(map(int, input().split(' ')))
    lst_list.append(lst)
    
lst_list.sort(key = lambda x : (x[1],x[0]))

end_lst = []
for i in range(n):
    end_lst.append(lst_list[i][1])

cnt = 1
end_idx = 0

#끝 시간 정렬만 하고 해보기 
for i in range(1,n)  :
    if lst_list[i][0] >= end_lst[end_idx]:
        cnt += 1
        end_idx = i

print(cnt)