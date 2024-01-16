# 2914
import math
A, I = map(int, input().split())

melody = 1
while True:
    if math.ceil(melody/A) == I :
        print(melody)
        break
    else :
        melody += 1
