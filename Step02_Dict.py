# dict type

'''
1. key:value
2. 순서없음
3. key 값을 이용해 저장된 값을 참조

'''

# 회원 1명의 데이터, 리스트[]에 담으면 쓰기 불편.
mem1 = {"num":1, "name":"kimgura", "isMan":True}
print(mem1["num"])
print(mem1["name"])
print(mem1["isMan"])

#dict  안에 내용을 참조해서 변수에 담기
a = mem1["num"]
b = mem1["name"]
c = mem1["isMan"]

#dict 안의 내용을 수정하기
mem1["num"] =2
mem1["name"]="parkdajeong"
mem1["isMan"]=False

print("종료합니다")

#특정 KEY 값으로 저장된 내용 삭제
del mem1["isMan"]

#모든 값 삭제
mem1.clear()

print("종료")
