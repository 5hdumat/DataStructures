'''
이진 검색(binary search)

이진 검색 알고리즘을 사용하려면 배열의 데이터가 정렬되어 있어야 한다. (참고로 선형 검색보다 검색 속도가 빠르다)

1. x = [5, 7, 15, 28, 29, 31, 39, 58, 68, 70, 95] 와 같이 정렬된 배열에서 찾고자 하는 원소를 39라고 가정해보자.
2. 이진 검색은 정중앙에 위치한 원소 31에 주목한다.
3. 찾아야 할 원소 39는 31보다 뒤쪾에 존재하므로 검색 대상을 x[6] ~ x[10]으로 좁힌다.
4. 반복한다.

이진 검색 알고리즘은 검색을 반복할 때마다 검색 범위가 거의 절반으로 줄어들며, 시간 복잡도는 logN이다.
검색에 실패할 경우 log(N+1), 검색에 성공할 경우 log(N-1)이다.

'''
from typing import Sequence, Any


def binary_search(seq: Sequence, key: Any) -> int:
    pl = 0
    pr = len(seq) - 1

    while pl <= pr:
        pc = (pl + pr) // 2

        if seq[pc] == key:
            return pc

        if seq[pc] > key:
            pr = pc - 1

        if seq[pc] < key:
            pl = pc + 1

        print(pc, pl, pr)

    else:
        return -1

if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요.: '))

    x = [None] * num


    print('배열의 데이터를 오름차순으로 입력해주세요.')

    x[0] = int(input(f'x[{0}]: '))
    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}]: '))

            if x[i] > x[i - 1]:  # 바로 직전에 입력한 값보다 큰 값을 입력하면 다음 입력으로 넘어감
                break

    key = int(input('검색할 값을 입력하세요.: '))

    idx = binary_search(x, key)

    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색 값은 {idx}에 있습니다.')

