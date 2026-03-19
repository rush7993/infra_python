#

'''

json, xml, yaml

'''
#info는 str type, 문자열이 특별한형식(json)
import json


info = '''{
    "name":"박다정",
    "addr":"목포",
    "foods":["딸기","복숭아"]
}'''

#json을 dict 로
result = json.loads(info)
#dict ->json 문자열로 변환
result2 = json.dumps(result)




print("종료됨")
