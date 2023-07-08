heights = []
heights_sum = 0
for i in range(9):
    height = int(input())
    heights_sum += height
    heights.append(height)
    
heights.sort()

is_ok = False
for first in range(9):
    for second in range(first, 9):
        if first == second:
            continue  #Pass : 골격 맞추는 느낌, 나중에 채울 거니까 기다려, #continue는 아무것도 안 한다는 의미라서 둘이 좀 다름
        height_total = heights_sum - heights[first] - heights[second]
        if height_total == 100:
            heights.remove(heights[second])
            heights.remove(heights[first])
            is_ok = True
            break
    if is_ok:
        break

for i in range(len(heights)): 
    print(heights[i])


