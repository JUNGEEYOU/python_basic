"""
 5. dict 자료형
"""

data = dict()
data['apple'] ='사과'
data['banana'] = '바나나'

print(data)      # {'apple': '사과', 'banana': '바나나'}

if 'apple' in data:     # 특정 원소 존재 확인
    print('사과가 존재함')

key_list = data.keys()
val_list = data.values()
print(key_list)        # dict_keys(['apple', 'banana'])
print(val_list)        # dict_values(['사과', '바나나'])

for key in key_list:
    print(data[key])   # 사과 바나나

for k, v in data.items():  # key, vlaue 모두 얻음
    print(k,v)