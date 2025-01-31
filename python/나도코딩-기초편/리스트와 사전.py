# 리스트

aList = [1, 2, 3]
bList = [4, True, "유재석"]

aList.extend(bList)

print(aList)


# 사전

cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))



cabinet2 = {"key1":"value1", "key2":"value2"}
print(cabinet2["key1"])
print(cabinet2.get("key1"))

cabinet2.clear()

