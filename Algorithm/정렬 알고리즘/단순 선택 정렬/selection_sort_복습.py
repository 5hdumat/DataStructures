def selection_sort(x):
    for i in range(num - 1):
        min = i  # 일단 i가 가장 작은 값이라고 가정

        for j in range(i + 1, num):
            if x[j] < x[min]:
                min = j

        x[min], x[i] = x[i], x[min]


if __name__ == '__main__':
    num = int(input('원소의 개수를 입력하세요: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    selection_sort(x)

    print(x)
