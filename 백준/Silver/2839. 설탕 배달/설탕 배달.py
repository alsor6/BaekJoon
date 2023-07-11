N = int(input())
count = 0

if N%5 == 0 :
    a = N//5
    count = a
    print(count)
    
else:
    while N > 0 :
        N -= 3
        count += 1
        
        if N%5 == 0:
            a = N//5
            count += a
            print(count)
            break 
            
        else:
            if N == 1 or N == 2 :
                print(-1)
                break