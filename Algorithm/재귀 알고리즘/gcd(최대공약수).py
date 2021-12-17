'''
유클리드 호제법을  이용한 최대 공약수 구하기

[유클리드 호제법]
비교대상의 두 개의 자연수 a, b(단, a > b)가 있을 때 a를 b로 나눈 나머지를 r이라고 가정한 후
gcd(a, b)는 = gcd(b, r)과 같다는 공식이다.
이 과정을 반복하다보면 r이 0이 나오게 되는데 그때 b가 a와 b의 최대공약수가 된다는 원리이다.
'''
import math

def gcd(x: int, y: int) -> int:
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


x = int(input('첫 번째 정숫값을 입력하세요:'))
y = int(input('두 번째 정숫값을 입력하세요:'))

print(f'{x}와 {y}의 최대 공약수는 {gcd(x, y)} 입니다.')
print(f'{x}와 {y}의 최대 공약수는 {math.gcd(x, y)} 입니다.')
