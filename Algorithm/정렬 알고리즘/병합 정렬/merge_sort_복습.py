def merge_sort(x):
    def _merge_sort(x, left, right):
        if left < right:
            center = (left + right) // 2

            _merge_sort(x, left, center)
            _merge_sort(x, center + 1, right)

            bp = bk = 0
            mp = mk = left

            while mp <= center:
                buff[bp] = x[mp]
                bp += 1
                mp += 1

            while mp <= right and bk < bp:
                if buff[bk] < x[mp]:
                    x[mk] = buff[bk]
                    bk += 1
                else:
                    x[mk] = x[mp]
                    mp += 1
                mk += 1

            while bk < bp:
                x[mk] = buff[bk]
                bk += 1
                mk += 1

    buff = [0] * n
    _merge_sort(x, 0, n - 1)
    del buff


if __name__ == '__main__':
    n = int(input('원소 수를 입력해주세요.: '))
    x = [None] * n

    for i in range(n):
        x[i] = int(input(f'x[{i}]: '))

    merge_sort(x)

    for i in range(n):
        print(f'x[{i}] = {x[i]}')
