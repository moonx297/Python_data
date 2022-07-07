# 리스트의 탐색과 삭제
# 탐색
heroes = ["아이언맨", "토르","헐크","스칼렛", "토르"]
n = heroes.index("헐크")
print(n)

# 삭제 -> pop(인덱스)로
heroes = ["아이언맨", "토르", "헐크"]
h = heroes.pop(1)
print(heroes)

# 삭제 ->데이터로
heroes = ["아이언맨", "토르", "헐크"]
h = heroes.remove("아이언맨")
print(heroes)