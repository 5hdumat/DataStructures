'''
선형 검색은 기본적으로 2가지 판단 조건을 가진다.

1. 검색할 값을 찾지 못하고 배열의 맨 끝을 지나갔습니까?
2. 검색할 값과 같은 원소를 찾으셨습니까?

하지만 수 많은 반복을 진행하면서 이러한 판단 조건을 계속 수행해야 하는 비용을 무시할 순 없다.
이러한 비용을 줄이고자 탄생한 것이 보초법이다.

x = [1, 2, 3, 4, 5] 라는 배열에서 찾고자 하는 원소가 3이라고 가정한다면 x배열의 맨 끝에 원소 3을 append 한다.
x = [1, 2, 3, 4, 5] -> x = [1, 2, 3, 4, 5, 3]

이렇게 되면 검색 판단 조건 중 '1. 검색할 값을 찾지 못하고 배열의 맨 끝을 지나갔습니까?'를 사용하지 않아도 된다.
이제는 판단 횟수를 절반으로 줄일 수 있다.
'''

# 선현 검색 알고리즘을 보초법으로 수정
import copy
from typing import Any, Sequence


def seq_search(seq: Sequence, key: Any) -> int:
    tmp = copy.deepcopy(seq)  # seq를 깊은 복사한다. (리스트는 뮤터블하므로 전달받은 인자를 수정하면 원본 데이터도 변경되므로 깊은 복사를 해야한다.)
    tmp.append(key)  # 보초 key 추가

    i = 0

    while True:
        if tmp[i] == key: # 보초법으로 인해 종료조건이 2개에서 1개로 줄어들었다. 따라서 반복문을 종료하기 위한 판단 횟수가 절반으로 줄어든다.
            break

        i += 1

    return -1 if i == len(seq) else i # 찾은 원소가 찾고자 하는 원소인지 보초인지 판단


if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i:}]: '))

    key = int(input('검색할 값을 입력하세요: '))

    idx = seq_search(x, key)

    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색 값은 {idx}에 있습니다.')
