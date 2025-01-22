from random import *
import sys

total_people = 50


count = 0
for num in range(1, 51) :

    time = randint(5, 50)

    if time <5 or time > 15 :
        print(f"[ ]\t{num}번째 손님 \t(소요시간 : {time}분)")
    else :
        count+=1
        print(f"[O]\t{num}번째 손님 \t(소요시간 : {time}분)")

print("총 탑승 승객 : {0} 분" .format(count))
