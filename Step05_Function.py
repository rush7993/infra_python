# 
"""
function type

- 특정 시점에 여러줄 code를 일괄실행
- 함수도 data 타입(변수에 담을 수 있음)
- 일괄실행 하는 것을 call 이라함.
- 함수는 저장된 code를 다 실행하고 나면 원래 call했던 위치로 넘어옴.
- call했던 위치로 돌아오면서 데이터를 반드시 가져옴.
"""

def test1():
    print("test1() 호출됨")

test1()
result1 = test1()

def test2(arg):
    print("전달받은내용:", arg)
    print(f"전달받은내용: f중괄호는이어붙여봐{arg} ")

test2(None)
test2(20)
test2("kim")


def print_sum(num1, num2):
    sum = num1+num2
    print(f"{num1} +{num2} = {sum}")

print_sum(10,20)

def print_info(name: str, addr: str):
    print(f"이름은 {name} 이고 주소는 {addr}")

print_info("김구라","노량진")
print_info(addr="행신동", name="해골")

print("종료")

