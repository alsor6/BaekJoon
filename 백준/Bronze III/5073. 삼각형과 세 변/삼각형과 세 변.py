# 5073
while True : 
    a, b, c = map(int, input().split())
    if a == b == c == 0 :
        break
    else :
        if max(a,b,c) == a :
            if a >= b+c :
                print('Invalid')
            elif a == b == c :
                print('Equilateral')
            elif (a == b and b != c) or (b == c and c != a) or (a == c and a != b) :
                print('Isosceles')
            elif a != b and b != c and c != a:
                print('Scalene')
        elif max(a,b,c) == b : 
            if b >= a+c :
                print('Invalid')
            elif a == b == c :
                print('Equilateral')
            elif (a == b and b != c) or (b == c and c != a) or (a == c and a != b) :
                print('Isosceles')
            elif a != b and b != c and c != a:
                print('Scalene')
                
        elif max(a,b,c) == c :
            if c >= a+b :
                print('Invalid')
            elif a == b == c :
                print('Equilateral')
            elif (a == b and b != c) or (b == c and c != a) or (a == c and a != b) :
                print('Isosceles')
            elif a != b and b != c and c != a:
                print('Scalene')
