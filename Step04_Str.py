#str type

#양쪽에 공백이 포함되거나 포함될 가능성이 있는 문자열 있다고 가정
#공백제거
text = "    cloud infra "
result1 =text.strip()

myIp = "192.168.0.2"
result2 = myIp.split(".")

#join
result3 = ".".join(result2)


#특정 문자열 찾아서 대체하기
result4 = "hello dj!".replace("dj","dajeong")

result5 = "python".upper()
result6 = "PYTHON".lower()

print("제거완료")