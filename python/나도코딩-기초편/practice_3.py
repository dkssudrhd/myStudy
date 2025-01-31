site = "http://naver.com"

rule1 = site[7:]
rule2 = rule1[:rule1.find(".")]

# i = 0
# eCount = 0
# while True :
#     i = rule2.find("e", i+1)
#     if i == -1 :
#         break
#     else :
#         eCount += 1


eCount = rule2.count("e")

rule3 = rule2[:3] + str(len(rule2)) + str(eCount) + "!"

print(site)
print(rule1)
print(rule2)
print(rule3)

print(f"생성된 비밀번호 : {rule3}")
