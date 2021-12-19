def insertion_sort(x):
    for i in range(1, n):
        key = x[i]
        j = i

        while j > 0 and key < x[j]:
            x[j] = x[j - 1]
            j -= 1

        x[j] = key


def binary_insertion_sort(x):
    for i in range(1, n):
        key = x[i]
        pl = 0
        pr = i - 1

        while True:
            pc = (pl + pr) // 2

            if x[pc] == key:
                break
            elif x[pc] < key:
                pl = pc + 1
            else:
                pr = pc - 1

            if pl > pr:
                break

        if pl <= pr:
            pd = pc + 1
        else:
            pd = pr + 1

        for j in range(i, pd, -1):
            x[j] = x[j - 1]

        x[pd] = key


if __name__ == '__main__':
    n = int(input('원소의 개수를 입력하세요: '))
    x = [None] * n

    for i in range(n):
        x[i] = int(input(f'x[{i}]: '))

    binary_insertion_sort(x)

    print(x)
