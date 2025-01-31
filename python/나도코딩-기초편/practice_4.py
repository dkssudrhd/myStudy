from random import * 
# member = []

# for i in range(20) :
#     member.append(i+1)

members = range(1, 21)
print(type(members))

members = list(range(1, 21))

shuffle(members)

chicken = sample(members, 1)
members.remove(chicken[0])

coffee = sample(members, 3)

print(f"치킨 당첨자 : {chicken[0]}")
print(f"커피 당첨자 : {coffee}")