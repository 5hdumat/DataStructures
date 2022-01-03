def shaker_sort(x):
    left = 0
    right = num - 1
    last = right

    # 홀수 패스
    while left < right:
        for i in range(right, left, -1):
            for j in range(right, right - i, -1):
                if x[j] < x[j - 1]:
                    x[j], x[j - 1] = x[j - 1], x[j]
                    last = j

        left = last

        for i in range(left, right):
            for j in range(left, right - i):
                if x[j] > x[j + 1]:
                    x[j], x[j + 1] = x[j + 1], x[j]
                    last = j

        right = last


if __name__ == '__main__':
    num = int(input('원소의 개수를 입력하세요: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    shaker_sort(x)

    print(x)
