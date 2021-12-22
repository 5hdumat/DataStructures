def qsort(x, left, right):
    ql = left
    qr = right
    pivot = x[(left + right) // 2]

    while ql <= qr:
        while x[ql] < pivot:
            ql += 1

        while x[qr] > pivot:
            qr -= 1

        if ql <= qr:
            x[ql], x[qr] = x[qr], x[ql]
            ql += 1
            qr -= 1

    if left < qr:
        qsort(x, left, qr)

    if ql < right:
        qsort(x, ql, right)


if __name__ == '__main__':
    print('배열을 나눕니다.')
    n = int(input('원소 수를 입력해주세요.: '))
    x = [None] * n

    for i in range(n):
        x[i] = int(input(f'x[{i}]: '))

    qsort(x, 0, n - 1)

    print(x)
