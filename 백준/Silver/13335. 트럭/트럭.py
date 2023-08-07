#13335 트럭
from collections import deque
queue = deque()

##함수부
def find_time():
    time = 0
    while truck_queue:
        bridge.popleft()
        if(sum(bridge)+truck_queue[0]) <= L:
            truck = truck_queue.popleft()
            bridge.append(truck)
        else:
            bridge.append(0)
        time += 1
    time = time + w
    print(time)
    return

##코드부    
n, w, L = map(int, input().split())
truck_lst = list(map(int, input().split()))
truck_queue = deque()
bridge = deque([0]*w)
for i in truck_lst:
    truck_queue.append(i)
find_time()