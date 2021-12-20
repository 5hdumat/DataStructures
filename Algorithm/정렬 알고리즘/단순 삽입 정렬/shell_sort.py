'''
셸 정렬은 단순 삽입 정렬의 장점을 살리고 단점은 보오나하여 더 빠르게 정렬하는 알고리즘이다.
셸 정렬은 먼저 정렬할 배열의 원소를 그룹으로 나워 각 그룹별로 정렬을 수행한다. (이웃한 원소와 비교하지 않으므로 안정적이지 않은 정렬을 수행한다.)

[8, 1, 4, 2, 7, 6, 3, 5]

1. 위 배열을 예에서 4칸씩 떨어진 원소를 4개의 그룹으로 나눈다.

(8, 7) (1, 6) (4, 3) (2, 5)

2. 그리고 정렬한다.

(7, 8) (1, 6) (3, 4) (2, 5)

3. 아래와 같은 배열이 완성된다.

[7, 1, 3, 2, 8, 6, 4, 5]

4. 이제 2칸씩 떨어진 원소를 2개의 그룹으로 나눈다. 그리고 다시 정렬한다.
(7, 3, 7, 4) (1, 2, 6, 5)

5. 다음으로 1칸씩 떨어진 원소를 다시 정렬한다. (4-2-1 순으로 h-정렬)

7번의 정렬은 모두 단순 삽입 정렬
정렬 횟수는 늘어나지만 전체적으로 원소의 이동 횟수가 줄어들어 효율적이다.
'''

from typing import MutableSequence


# (입력 h = 4)
# 8 1 4 2 7 6 3 5
# (4-sort 후, h = 2)
# 7 1 3 2 8 6 4 5

def shell_sort(x: MutableSequence):
    h = num // 2

    while h > 0:
        for i in range(h, num):
            j = i - h

            tmp = x[i]

            while j >= 0 and x[j] > tmp:
                x[j + h] = x[j]
                j -= h

            x[j + h] = tmp

        h //= 2


'''
이 정렬을 조금 더 효율적으로 사용하려면 h 값이 서로 배수가 되지 않도록 해야 한다.
h 값이 서로 배수가 되지 않아야 충분히 원소들이 뒤섞이기 때문이다.

주의점) h의 초깃값이 지나치게 크면 효과가 없다. 따라서 배열의 원소 수인 n을 9로 나누었을 때 그 몫을 넘지 않도록 해야한다.
원소수가 적으면 셸 정렬이 크게 의미가 없으므로 8개 기준 h가 1이 된다. 즉 원소가 적을 땐 단순 삽입 정렬로 수행된다.
'''


def shell_sort2(x: MutableSequence):
    h = 1

    while h < num // 9:
        h = h * 3 + 1

    while h > 0:
        print('hhhh', h)
        for i in range(h, num):
            j = i - h
            tmp = x[i]

            while j >= 0 and x[j] > tmp:
                print(x[j + h], x[j])
                x[j + h] = x[j]
                j -= h

            x[j + h] = tmp
            print(x[j + h], tmp)

            print(x)

        # h //= 2
        h //= 3


if __name__ == '__main__':
    print('셸 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요: '))

    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    shell_sort2(x)

    print('오름차순 정렬을 수행했습니다.')

    for i in range(num):
        print(f'x[{i}] = {x[i]}')
