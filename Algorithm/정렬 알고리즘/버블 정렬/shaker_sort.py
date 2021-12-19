def shaker_sort(x):
    left = 0
    right = len(x) - 1
    i = 0
    while left < right:
        # 홀수 패스에서는 가장 작은 원소를 맨 앞으로 이동 시키고
        for j in range(right, left, -1):
            if x[j - 1] > x[j]:
                x[j - 1], x[j] = x[j], x[j - 1]
            left = j

        # 짝수 패스에서는 가장 큰 원소를 맨 뒤로 이동시킨다.
        for j in range(left, right):
            if x[j] > x[j + 1]:
                x[j + 1], x[j] = x[j], x[j + 1]
            right = j

        i += 1


if __name__ == '__main__':
    num = int(input('원소의 개수를 입력하세요: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    shaker_sort(x)

    print(x)
