"""
 1. 수 자료형
  1) 정수형: 양의 정수, 음의 정수
  2) 실수형
   - 1e9 : 10억. e는 10의 지수 승
   - 소수점 주의: 소수점 비교 시 round 함수 이용

 2. 수 연산
   - 나누기: /, %, //
   - 거듭제곱: **
"""
# 1. 수 자료형
# 2) 실수형
# - 1e9 사용
a = 1e9
print(a)     # 1000000000.0

a = 75.25e1
print(a)     # 752.5

a = 2954e-3
print(a)     # 2.954


# - 소수점 주의점
a = 0.3 + 0.6
print(a)                    # 0.8999999999999999
print(round(a, 1))          # 0.9
if round(a, 1) == 0.9:
    print(True)             # True


# 2. 수 연산
# - 나누기
a = 7
b =3

print(a / b)        # 나누기. 2.3333333333333335
print(a % b)        # 나머지. 1
print(a // b)       # 몫.   2

# - 거듭제곱
print(a**b)         # 거듭제곱. 343
