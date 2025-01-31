
# try :
#     print("나누기 전용 계산기 입니다.")
#     nums = []
#     nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
#     nums.append(int(nums[0] / nums[1]))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# except ValueError as err:
#     print("{0} 에러! 잘못된 값을 입력하였습니다.".format(err))
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print("{0} 알수 없는 에러가 발생하였습니다.".format(err))

class BigNumberErr(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try :
    print("한 자리 숫자 나누기 전용 계산기 입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    if nums[0] >= 10 or nums[1] >= 10:
        raise BigNumberErr("입력값 : {0}, {1}".format(nums[0], nums[1]))
    nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except BigNumberErr as err:
    print("{0} 잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.".format(err))

