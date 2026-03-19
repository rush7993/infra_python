#
'''
- tuple (value", value2, value3,...)
1. list type과 유사
2. 읽기 전용(수정, 삭제 불가)
3. 기능이 적기 때문에 처리속도가 빠르다

'''

from calendar import firstweekday


tuple1: tuple =("one","two","three")
result1 = tuple1[0]

print("종료")

#readonly 수정,삭제,추가 불가!!


# 1개짜리 tuple 컴마가 필요함, 문자로 만들어짐주의
tuple2=("김구라",)

#괄호 없는 튜플
tuple3 = 10, 20, 30

# tuple에 저장된 값을 여러 변수에 나누어 담기
a,b,c = tuple3

# 두 변수 값 서로 교환
fisrt = "girl"
second = "boy"
'''
tmp=first
first=second
second=tmp
'''
first, second = second, first





print("주의")