#

# 다중 if문 구성

"""
디스트 사용률 입력(조사) 90이상이면

디스크 용량 부족

70 이상이면
 디스크 사용량이 높다. 확장을 준비하세요

 그 외에는
 정상입니다.
"""

disk_usage:int = int(input("디스크 사용률 입력(0-100):"))

if disk_usage >= 90:
    print("용량부족")
elif disk_usage >=70:
    print("사용량이 높습니다.확장을 준비하세요")
else:
    print("정상")

