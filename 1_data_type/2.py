"""
 2. 리스트 자료형
 - 리스트 초기화
 - 리스트의 인덱싱과 슬라이싱열
 - 리스트 컴프리핸션
 - 리스트 관련 기타 메소드
"""

# 리스트 초기화
n = 10
a = [0] * n
print(a)      # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# 리스트의 인덱싱과 슬라이싱
# -1를 인덱스에 넣으면 가장 마지막 원소가 출력된다.

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[-1])       # 9. 가장 마지막 원소
print(a[-3])       # 7

a[3] = 7
print(a)           # [1, 2, 3, 7, 5, 6, 7, 8, 9]
print(a[1:4])      # [2, 3, 7]

# 리스트 컴프리핸션
array = [i for i in range(20) if i % 2 == 1]
print(array)       # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

array = [i*i for i in range(1, 9)]
print(array)       # [1, 4, 9, 16, 25, 36, 49, 64]

n = 3
m = 4
array = [[0] * m for _ in range(n)]   # n * m 2 차원 배열 초기화. array = [[0]*m] * n 은 문제가됨.
print(array)


# 리스트 관련 기타 메소드
a = [1, 4, 3]
print(a)           # [1, 4, 3]

a.append(2)
print(a)           # [1, 4, 3, 2]

a.sort()
print(a)           # [1, 2, 3, 4]

a.sort(reverse=True)
print(a)           # [4, 3, 2, 1]

a.reverse()
print(a)           # [1, 2, 3, 4]

a.insert(2, 3)
print(a)           # [1, 2, 3, 3, 4]

print(a.count(3))  # 2

a.remove(3)
print(a)     # [1, 2, 3, 4]

# 특정 원소를 포함 하지 않고 담기
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}
result = [i for i in a if i not in remove_set]
print(result)          # [1, 2, 4]

