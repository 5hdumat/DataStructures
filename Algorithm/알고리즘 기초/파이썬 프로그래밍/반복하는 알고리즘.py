'''
판단 반복 구조 (while)
참고로 파이썬은 do~while, repeat~until 등의 사후 판단 반복문을 지원하지 않는다.
'''
n = int(input())
sum = 0
i = 1

while i <= n:
    sum += i
    i += 1

print(sum)

'''
1부터 n까지의 합은 수학식 n * (n+1) // 2로도 구할 수 있다.
'''

n = int(input())
print(n * (n + 1) // 2)

'''
범위 입력받아 정수의 합 구하기 (for)
'''
a, b = map(int, input().split())

# a와 b 오름차순 정렬을 위해 단일 대입문 사용
if a > b:
    a, b = b, a

sum = 0
for i in range(a, b + 1):
    sum += i

print(sum)

'''
직각이등변삼각형 호출하기
'''
n = int(input())
for i in range(n):
    for j in range(i + 1):
        print('*', end='')
    print()

# 우측 정렬 삼각형
n = int(input())
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
    for j in range(i + 1):
        print('*', end='')
    print()
