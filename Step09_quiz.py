#

'''
    비밀번호 입력받아서 8자 이상이면 
    사용가능
    그렇지 않으면
    사용불가
'''

password: str = input("패스워드를 입력하세요:" )

if len(password) >= 8:
    print("사용가능")
else:
    print("사용불가")
