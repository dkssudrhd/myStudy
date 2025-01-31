
for num in range(1, 51):
    file = open("나도코딩/test/"+str(num)+"주차.txt", "w", encoding="utf8")
    file.write("- {0} 주차 주간보고 - \n".format(str(num)))
    file.write("부서 : \n")
    file.write("이름 : \n")
    file.write("업무 요약약 : \n")
    
    file.close()

