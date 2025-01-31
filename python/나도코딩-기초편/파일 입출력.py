

# 파일 새로 만들고 내용 적기
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)

# score_file.close


# 파일 내용 추가하기
# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80\n")
# score_file.write("코딩 : 100")

# score_file.close()

# 파일 읽어오기
# score_file = open("score.txt", "r", encoding="utf8")

# #전체 읽기
# print(score_file.read())
# 한줄읽고 커서를 다음 줄로 이동
# print(score_file.readline())

# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line)


# score_file.close()


# import pickle
# profile_file = open("procile.pickle", "wb")
# profile = {"이름" : "박명수", "나이" : 30, "취미" : ["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file)

# profile_file.close()

# profile_file = open("procile.pickle", "rb")
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()

# with open("procile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))


# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 공부하고 있어요")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())


