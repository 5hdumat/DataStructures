from fixed_stack import FixedStack


# 피벗 기준으로 그룹 나누기
def qsort_partition(x):
    pl = 0
    pr = n - 1
    pivot = x[(pl + pr) // 2]

    while pl <= pr:
        while x[pl] < pivot:
            pl += 1

        while x[pr] > pivot:
            pr -= 1

        if pl <= pr:
            x[pl], x[pr] = x[pr], x[pl]
            pl += 1
            pr -= 1


# 재귀로 퀵 소트 구현하기
def qsort_recur(x, left, right):
    pl = left
    pr = right
    pivot = x[(left + right) // 2]

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
        qsort_recur(x, left, pr)

    if pl < right:
        qsort_recur(x, pl, right)


# 재귀 없이 스택으로 퀵 소트 구현하기
def qsort_non_recur(x, left, right):
    stk = FixedStack(n)
    stk.push((left, right))

    while not stk.is_empty():
        pl, pr = left, right = stk.pop()
        pivot = x[(left + right) // 2]

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

    qsort_non_recur(x, 0, n - 1)

    print(x)
