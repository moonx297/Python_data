# 리스트 최소/ 최대값 및 정렬
# 최소값 최대값
values = [1,2,3,4,5,6,7,8,9]
print("min = ", min(values))
print("max = ", max(values))

# 정렬 1 - 자체가 바뀐거
a = [3,2,1,5,4]
a.sort()
print(a)

# 정렬 2 - 정렬한 데이터를 넘겨준거 (desc / asc)
numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
ascending_number = sorted(numbers)
print(numbers)
print(ascending_number)