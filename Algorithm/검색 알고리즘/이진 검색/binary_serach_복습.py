def binary_search(x, key):
    pl = 0
    pr = num - 1

    while True:
        pc = (pl + pr) // 2

        if x[pc] == key:
            return pc
        elif x[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1

        if pl > pr:
            break


if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요.: '))

    x = [None] * num

    print('배열의 데이터를 오름차순으로 입력해주세요.')

    x[0] = int(input(f'x[{0}]: '))
    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}]: '))

            if x[i] > x[i - 1]:  # 바로 직전에 입력한 값보다 큰 값을 입력하면 다음 입력으로 넘어감
                break

    key = int(input('검색할 값을 입력하세요.: '))

    idx = binary_search(x, key)

    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색 값은 {idx}에 있습니다.')
