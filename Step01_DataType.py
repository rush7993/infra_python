#한줄주석

"""
여러줄 주석
"""

print("Step01 시작")

#python 데이터타입

#int
num1 = 10
#float
num2 = 10.1
#str
myName = '김구라'
yourName = "해골"
ourName = """
    KT Cloud Infra
    화이팅!
"""

print(myName)

#순서중요
foods=["복숭아","딸기","귤"] #list
print(foods)

#순서중요x {key:value}
mem1 = {"num":1, "name":"김구라", "addr": "노량진"} #dict
print(mem1)

#순서중요x 하나의 묶음으로 관리(키값 x)
mySet = {" 빨강","파랑","노랑"} #set
print(mySet)

#특정 code 블럭을 필요한 시점에 일괄실행
def store():
    print("냉장고 문 연다")
    print("물건 저장한다")
    print("냉장고 문 닫는다")

store()



# 어떤 변수를 빈 상태로 만들고 값을 나중에 넣고 싶다면? None
a = None
print("어떤 작업을 하고")
print("필요하라 때 값 넣기")
a = "test"


# 참과 거짓을 나타내는 data type (Bool) 
# isxxx
# canXXX형태
isMan=True
isWoman=False
isDifferent=True
isRun=False
canEat=True

