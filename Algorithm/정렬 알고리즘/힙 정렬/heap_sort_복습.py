def heap_sort(x):
    def down_heap(x, left, right):
        tmp = x[left]
        parent = left

        while parent < (right + 1) // 2:
            cl = parent * 2 + 1
            cr = parent * 2 + 2

            if cr <= right and x[cl] < x[cr]:
                child = cr
            else:
                child = cl

            if tmp >= x[child]:
                break

            x[parent] = x[child]
            parent = child

        x[parent] = tmp

    for i in range((n - 1) // 2, -1, -1):
        down_heap(x, i, n - 1)

    for i in range(n - 1, 0, -1):
        x[0], x[i] = x[i], x[0]
        down_heap(x, 0, i - 1)


if __name__ == '__main__':
    n = int(input('원소 수를 입력하세요: '))
    x = [None] * n

    for i in range(n):
        x[i] = int(input(f'x[{i}]: '))

    heap_sort(x)

    for i in range(n):
        print(f'x[{i}] = {x[i]}')
