'''
재귀를 사용하는 대표적인 예로 양의 정수 곱을 구하는 팩토리얼이 있다.
팩토리얼은 양의 정수를 순차적으로 곱한다하여 '순차곱셈'이라고도 한다.
(물론 팩토리얼 함수는 재귀 함수로 정의하지 않는 것이 간단하고 효율적이지만 재귀의 원리를 이해하는게 주 목적)

참고: 파이썬에서는 팩토리얼 값을 구해주는 표준 라이브러리로 math 모듈에서 factorial 함수를 제공한다.
'''
import math

def factorial(n: int) -> int:
    '''
    [4 입력]

    0) 정답 24
    1) 4 * factorial(3) :: 복귀된 6 반환 -> 24으로 복귀
    1) 3 * factorial(2) :: 복귀된 2 반환 -> 6으로 복귀
    2) 2 * factorial(1) :: 복귀된 1 반환 -> 2로 복귀
    3) 1 * factorial(0) :: 복귀된 1 반환 -> 1로 복귀
    4) n이 0 이므로 return 1 (다시 복귀주소로 거슬로 올라간다.)
    '''
    if n > 0:
        return n * factorial(n - 1) # 동작과정 p.187 참고
    else:
        return 1


n = int(input('출력할 팩토리얼 값을 입력해주세요.: '))
print(f'펙토리얼 {n}의 값은 {factorial(n)} 입니다.')
print(f'펙토리얼 {n}의 값은 {math.factorial(n)} 입니다.')
