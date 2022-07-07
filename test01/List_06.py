# 성적 관리
STUDENT = 5
lst = []
count = 0

for i in range(STUDENT):
    value = int(input("성적을 입력하시오 : "))
    lst.append(value)

print("\n성적 평균=", sum(lst)/len(lst))
print("최고 점수=", max(lst)) #내장함수
print("최하 점수=", min(lst))

for score in lst:
    if score >= 80:
        count += 1
print("80점 이상 =", count)