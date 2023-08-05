def lotto(depth, idx):
    if depth == 6:
        print(*ret_list)
        return

    for jdx in range(idx, N):
        ret_list[depth] = lotto_list[jdx]
        lotto(depth+1,jdx+1)

ret_list = [0, 0, 0, 0, 0, 0]

for _ in range(6):
    num = list(map(int, input().split()))
    N = num[0]
    if N != 0 :
        lotto_list = list(num[1:len(num) + 1])
        lotto(0, 0)
        print()
    else :
         break
