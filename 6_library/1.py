# sum
result = sum([1, 2, 3])
print(result)        # 6

# min
result = min([1, 10, 3, 7])
print(result)        # 1

# max
result = max([1, 10, 3, 7])
print(result)        # 10

# sorted
result = sorted([1, 4, 10, 5, 0])
print(result)       # [0, 1, 4, 5, 10]

result = sorted([1, 4, 10, 5, 0], reverse=True)
print(result)       # [10, 5, 4, 1, 0]

# 튜플 2번째 값으로 정렬하고자 할때
result = sorted([('lena', 10), ('jake', 2), ('ray', 5)], key=lambda x: x[1], reverse=True)
print(result)