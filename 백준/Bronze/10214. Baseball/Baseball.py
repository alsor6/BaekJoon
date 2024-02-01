# 10214
T = int(input())
for i in range(T):
    K_score, Y_score = 0, 0
    for j in range(9) :  
        Y, K = map(int, input().split())
        Y_score += Y
        K_score += K
    if Y_score > K_score :
        print("Yonsei")
    elif Y_score < K_score :
        print("Korea")
    elif Y_score == K_score :
        print("Draw")