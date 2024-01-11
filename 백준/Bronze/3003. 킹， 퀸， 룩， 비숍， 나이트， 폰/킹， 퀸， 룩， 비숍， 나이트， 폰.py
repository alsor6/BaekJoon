# 3003
correct_piece = [1, 1, 2, 2, 2, 8]
have_now = list(map(int, input().split()))

for i in range(6) :
    need = correct_piece[i] - have_now[i]
    print(need, end=' ')

        
