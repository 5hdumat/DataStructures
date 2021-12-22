'''
스택을 활용해 비재귀적으로 퀵 정렬 만들기
'''
from fixed_stack import FixedStack


# 5 7 1 4 (6) 2 3 9 8
# 5 3 1 4 (6) 2 7 9 8
# 5 3 1 4 (2) 6 7 9 8

def qsort(x, left, right):
    stk = FixedStack(n)

    # 범위를 스택에 저장한다.
    # left, right는 나눠야 할 배열의 범위인 맨 앞 원소 인덱스와 맨 끝 원소 인덱스이다. p.267 참고
    stk.push((left, right))

    while not stk.is_empty():
        pl, pr = left, right = stk.pop()
        pivot = x[(left + right) // 2]

        print(pl, pr)
        while pl <= pr:
            while x[pl] < pivot:
                pl += 1

            while x[pr] > pivot:
                pr -= 1

            if pl <= pr:
                x[pl], x[pr] = x[pr], x[pl]
                pl += 1
                pr -= 1

        if left < pr:
            stk.push((left, pr))

        if pl < right:
            stk.push((pl, right))


if __name__ == '__main__':
    print('배열을 나눕니다.')
    n = int(input('원소 수를 입력해주세요.: '))
    x = [None] * n

    for i in range(n):
        x[i] = int(input(f'x[{i}]: '))

    qsort(x, 0, n - 1)

    print(x)
