def merge_sorted_list(a, b, c):
    pa, pb, pc = 0, 0, 0
    na, nb = len(a), len(b)

    while pa < na and pb < nb:
        # 배열 a의 a[pa]와 배열 b의 b[pb]를 주목하여 이 가운데 작은 값을 c[pc]에 저장
        if a[pa] <= b[pb]:
            c[pc] = a[pa]
            # 저장이 완료되었다면 커서를 하나 증가시켜 이동한다.
            pa += 1
        else:
            c[pc] = b[pb]
            pb += 1
        pc += 1

    # 배열 b의 모든 원소는 배열 c로 복사되었지만 아직 배열 a에 복사하지 않은 원소가 남아있으면 실행된다.
    while pa < na:
        c[pc] = a[pa]
        pa += 1
        pc += 1

    while pb < nb:
        c[pc] = b[pb]
        pb += 1
        pc += 1


if __name__ == '__main__':
    a = [2, 4, 6, 8, 11, 13]
    b = [1, 2, 3, 4, 9, 16, 21]
    c = [None] * (len(a) + len(b))
    # c = list(heapq.merge(a,b)) 로 대체 가능

    merge_sorted_list(a, b, c)

    print('배열 a와 b를 병합, 정렬하여 배열 c에 저장했습니다.')
    print(f'배열 a: {a}')
    print(f'배열 b: {b}')
    print(f'배열 c: {c}')
