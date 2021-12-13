# 리스트 역순으로 정렬하기
from typing import MutableSequence


def reverse_array(a: MutableSequence) -> None:
    n = len(a)

    for i in range(n // 2):
        a[i], a[n - i - 1] = a[n - i - 1], a[i]

if __name__ == '__main__':
    print('배열 원소를 역순으로 정렬합니다.')
    num = int(input('원소 수를 입력하세요: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]값을 입력하세요: '))

    print('배열 원소를 역순으로 정렬했습니다.')

    reverse_array(x)
    # 참고로 튜블은 이뮤터블하므로 자기 자신을 역순으로 정렬할 수 없다.

    # 리스트 역순 정렬
    # x.reverse()
    # 리스트 역순 정렬하여 새로 생성
    # x = list(reversed(x))

    for i in range(num):
        print(f'x[{i}] = {x[i]}')

