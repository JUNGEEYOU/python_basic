"""
 6. set 자료형
"""

# 초기화 방법
data = set([1, 1, 2, 3, 4, 4, 5])
print(data)                  # {1, 2, 3, 4, 5}

data = {1, 1, 2, 3, 4, 4, 5}
print(data)                  # {1, 2, 3, 4, 5}


# 집합 자료형의 연산
a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

print(a | b)   # 합집합. {1, 2, 3, 4, 5, 6, 7}
print(a & b)   # 교집합. {3, 4, 5}
print(a - b)   # 차집합. {1, 2}


# 집합 자료형 관련 함수
data = set([1, 2, 3])
print(data)    # {1, 2, 3}

data.add(4)
print(data)    # {1, 2, 3, 4}

data.update([5, 6])
print(data)    # {1, 2, 3, 4, 5, 6}

data.remove(3)
print(data)    # {1, 2, 4, 5, 6}