
# 줄바꿈할땐 마지막에 \
def profile(name, age = 20, main_lang ="python"):
    print("이름 : {0}\t 나이 : {1}\t 주요 언어 : {2}\t"\
          .format(name, age, main_lang))
    

profile("유재석")
profile("김태호", 21)
profile("정형돈", 22, "java")

profile(name="정준하", main_lang="c++", age=23)


