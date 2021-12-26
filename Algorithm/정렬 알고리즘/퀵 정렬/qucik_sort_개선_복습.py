def insertion_sort(x, left, right):
    for i in range(left + 1, right + 1):
        j = i
        tmp = x[j]

        while j > 0 and x[j - 1] > tmp:
            x[j] = x[j - 1]
            j -= 1

        x[j] = tmp


def pivot_sort(x, p1, p2, p3):
    if x[p1] > x[p2]:
        x[p1], x[p2] = x[p2], x[p1]

    if x[p2] > x[p3]:
        x[p2], x[p3] = x[p3], x[p2]

    if x[p1] > x[p3]:
        x[p1], x[p3] = x[p3], x[p1]

    return p2


def qsort(x, left, right):
    if right - left < 9:
        insertion_sort(x, left, right)

    else:
        pl = left
        pr = right
        m = pivot_sort(x, pl, (pl + pr) // 2, pr)
        pivot = x[m]

        x[m], x[pr - 1] = x[pr - 1], x[m]
        pl += 1
        pr -= 2
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
            qsort(x, left, pr)

        if pl < right:
            qsort(x, pl, right)


if __name__ == '__main__':
    n = int(input('원소 수를 입력해주세요.: '))
    x = [None] * n

    for i in range(n):
        x[i] = int(input(f'x[{i}]: '))

    qsort(x, 0, n - 1)

    print(x)
