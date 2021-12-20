def shell_sort(x):
    h = 1

    while h < n // 9:
        h = h * 3 + 1

    while h > 0:
        for i in range(h, n):
            j = i - h
            tmp = x[i]

            while j >= 0 and x[j] > tmp:
                x[j + h] = x[j]
                j -= h

            x[j + h] = tmp

        h //= 3


if __name__ == '__main__':
    n = int(input('원소의 개수를 입력하세요: '))
    x = [None] * n

    for i in range(n):
        x[i] = int(input(f'x[{i}]: '))

    shell_sort(x)

    print(x)
