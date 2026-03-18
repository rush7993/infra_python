#LIST TYPE
'''
1. 순서 중요 x
2. 여러 type 저장 가능
3. 값 변경 가능
'''
#대부분 한가지 타입을 담지만
#여러데이터타입 섞어 담기
datas=[10,"xxx",True]

datas.append(40)

#len() builtin  함수를 이용해서 LIST 의 길이를 얻을 수 있다.
nums=[10,20,30,40]
nums_len = len(nums)


#인덱스 참조
names=["김구라","해골","원숭이"]
name0 = names[0]
#인덱스 이용해서 삭제
del names[0]
#값에 의한 삭제
names.remove("원숭이")

#맨마지막 index를 삭제하면서 값 가져오기
nums.pop()
result = nums.pop()

print( "종료" )