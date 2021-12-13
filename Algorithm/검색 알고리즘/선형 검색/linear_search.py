'''
선형 검색 (linear search)

배열에서 검색하는 방법 중 가장 기본적인 알고리즘이다.
직선 모양(선형)으로 늘어선 배열에서 검색하는 경우 원하는 키값을 가진 원소를 찾을 때 까지 맨 앞에서 부터 스캔하여 순서대로 검색하는 알고리즘이다.

선형 검색에서 배열 스캔의 종료 조건은 다음과 같다.
- 검색할 값을 찾지 못하고 배열의 맨 끝을 지나간 경우 - 검색 실패
- 검색할 값과 같은 원소를 찾은 경우 - 검색 성공
'''
from typing import Any, Sequence

# 배열 a에서 값이 key인 원소를 선형 검색하는 함수
def seq_search(a: Sequence, key: Any) -> int:
    i = 0

    while True:
        if i == len(a):
            return -1 # 검색을 실패하여 -1 반환
            break

        if a[i] == key:
            return i # 검색에 성공하여 현재 검사한 배열의 인덱스를 반환
            break

        i += 1

# for 문을 이용하면 좀 더 간결하게 구현할 수 있다.
def seq_search_for(a: Sequence, key: Any) -> int:
    for i in range(len(a)):
        if a[i] == key:
            return i
    else:
        return -1

if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i:}]: '))

    key = int(input('검색할 값을 입력하세요: '))

    # idx = seq_search(x, key)
    idx = seq_search_for(x, key)

    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색 값은 {idx}에 있습니다.')
