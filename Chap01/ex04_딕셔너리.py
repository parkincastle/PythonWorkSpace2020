#딕셔너리 무가하기
a={1: 'a'}
a[2] = 'b' # {1: 'a', 2: 'b'}
print(a)

a['name'] = 'insung'
print(a) # {1: 'a', 2: 'b', 'name': 'insung'}

a[3] = [1, 2, 3]
print(a) # {1: 'a', 2: 'b', 'name': 'insung', 3: [1, 2, 3]}

#key값으로 value값 가져오기
print(a[1], a['name'], a[3]) # a insung [1, 2, 3]

#region딕셔너리 함수
print(a.keys()) # dict_keys([1, 2, 'name', 3])

for k in a.keys():
    print(k, end = ' ') # 1 2 name 3

print(list(a.keys())) # 1 2 name 3 [1, 2, 'name', 3]

print(a.values()) # dict_values(['a', 'b', 'insung', [1, 2, 3]])

#key, value값 쌍으로 가져오기
print(a.items()) # dict_values(['a', 'b', 'insung', [1, 2, 3]])

#모두 지우기
a.clear()
print(a) # {}

#key값으로 value값 얻기
print(a.get('name')) # None


