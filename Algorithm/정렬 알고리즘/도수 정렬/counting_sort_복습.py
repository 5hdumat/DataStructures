def counting_sort(x, max):
    f = [0] * (max + 1)
    b = [0] * n

    for i in range(n):
        f[x[i]] += 1

    for i in range(1, len(f)):
        f[i] += f[i - 1]

    for i in range(n - 1, -1, -1):
        f[x[i]] -= 1
        b[f[x[i]]] = x[i]

    for i in range(n):
        x[i] = b[i]


if __name__ == '__main__':
    n = int(input('원소 수를 입력해주세요: '))
    x = [None] * n

    for i in range(n):
        while True:
            x[i] = int(input(f'x[{i}]: '))
            if x[i] >= 0:
                break


    counting_sort(x, max(x))

    for i in range(n):
        print(f'x[{i}] = {x[i]}')
