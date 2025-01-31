
# sep 는 중간에 들어갈 내용을 설정가능
print("Python", "Java", sep=" vs ")

# end 는 print의 끝부분을 바꾸는 것  -> default는 \n임
print("Python", "Java", sep=" vs ", end="?")


import sys
print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)



# 시험 성적
scores = {"수학" : 100, "영어" : 70, "코딩" : 90}

# ljust(8) 왼쪽정렬인데 8칸을 차지하는 왼쪽 정렬
# rjust(4) 오른쪽정렬인데 4칸을 차지하는 오른쪽 정렬
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4))


# zfill(3) 은 1 -> 001
for num in range(1, 11):
    print("대기번호 : {0}".format(str(num).zfill(3)))

# 빈 자리는 빈 공간으로 두고 오른쪽 정렬은 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))

# 양수일땐 +로 음수일땐 - 로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<+10}".format(500))

# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(100000000000))

# 3자리 마다 콤마를 찍어주기, 부호
print("{0:+,}".format(100000000000))
print("{0:+,}".format(-100000000000))


# 3자리 마다 콤마를 찍어주고, 부호, 자릿수 확보
# 빈자리는 ^표시
print("{0:^<+30,}".format(100000000000000))

# 소수점 출력
print("{0:f}".format(5/3))

# 소수점 4째 자리까지만 표시(5째 자리에서 반올림)
print("{0:.4f}".format(5/3))