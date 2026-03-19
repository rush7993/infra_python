#yaml 형식의 문자열 다루기

#yaml 문자열을 다룰때는 외부 모듈을 pip로 설치를 해서 import 해야한다.

import yaml

#yaml  형식
info = '''
name: 박다정
addr: 목포
foods: 
  - 맥주
  - 치킨
isMan: true
body:
  weight: 77
  height: 177
'''

result = yaml.safe_load(info)
print(result)
print("세이프로드결과 딕트")

##과제 dict로 변환
info_dict = {
    "name": "박다정",
    "addr": "목포",
    "foods": ["맥주", "치킨"],
    "isMan": True,
    "body": {
        "weight": 77,
        "height": 177
    }
}

yaml_str = yaml.dump(info_dict, allow_unicode=True, sort_keys=True)
print(yaml_str)
print("야믈점덤프 결과 야믈")


##과제2 yaml로 변환
info_yaml="""
name: 박다정,
addr: 목 포,
foods:
  - 맥주
  - 치킨,
isMan: true,
body: {
  - weight: 77
  - height: 177
"""
print(info_yaml)

