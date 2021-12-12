# 배열 원소의 최댓값을 구해서 출력하기
import random
from max import max_of

print('난수의 최댓값을 구합니다.')
num = int(input('난수의 갯수를 입력해주세요.'))
x = [None] * num
lo = int(input('난수의 최솟값을 입력해주세요.'))
hi = int(input('난수의 최댓값을 입력해주세요.'))

for i in range(num):
    x[i] = random.randint(lo, hi)

print(x[:])
print(f'이 가운데 최댓값은 {max_of(x)} 입니다.')
