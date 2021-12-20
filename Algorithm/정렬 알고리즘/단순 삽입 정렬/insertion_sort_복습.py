def insertion_search(x):
    for i in range(1, n):
        j = i
        tmp = x[i]

        while j > 0 and x[j - 1] > tmp:
            x[j] = x[j - 1]
            j -= 1

        x[j] = tmp


# binary search를 활용한 선택 삽입 정렬 복습
def binary_insertion_search(x):
    for i in range(1, n):
        tmp = x[i]
        pl = 0
        pr = i - 1

        while True:
            pc = (pl + pr) // 2

            if x[pc] == tmp:
                break

            elif x[pc] > tmp:
                pr = pc - 1

            else:
                pl = pc + 1

            if pl > pr:
                break

        if pl <= pr:
            pd = pc + 1
        else:
            pd = pr + 1

        for j in range(i, pd, -1):
            x[j] = x[j - 1]

        x[pd] = tmp


if __name__ == '__main__':
    n = int(input('원소의 개수를 입력하세요: '))
    x = [None] * n

    for i in range(n):
        x[i] = int(input(f'x[{i}]: '))

    insertion_search(x)

    print(x)
