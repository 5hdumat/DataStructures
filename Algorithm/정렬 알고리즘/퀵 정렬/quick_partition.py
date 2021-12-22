'''
퀵 정렬은 가장 빠른 정렬 알고리즘이다.
이 알고리즘을 접하기에 앞서 배열을 두 그룹으로 나누는 연습을 해야 한다. 하단의 작업을 조금 더 발전시킨게 퀵 정렬 알고리즘이기 때문이다.

1. 배열을 두 그룹으로 나눠야 한다. 다음 배열에서 6을 피벗으로 선택하여 그룹으로 나눈다(n // 2, n=9)
pl      p       pr
5 7 1 4 6 2 3 9 8

2. 그 다음 피벗을 기준으로 피벗 이하의 원소들을 왼쪽으로 피벗 이상의 원소들을 오른쪽으로 정렬한다.

피벗 데이터보다 큰 원소가 나타날 때 까지 pl을 오른쪽 방향으로 스캔한다.
x[pl] <= p:
    pl += 1

피벗 데이터보다 작은 원소가 나타날 때 까지 pr을 왼쪽 방향으로 스캔한다.
x[pl] >= p:
    pr -= 1

'''

def partition(x):
    pl = 0
    pr = n - 1
    pivot = x[n // 2] # 원소 가운데 원소(피벗) 구하기

    print(pivot)
    while pl <= pr:
        while x[pl] < pivot:
            pl += 1

        while x[pr] > pivot:
            pr -= 1

        if pl <= pr:
            x[pl], x[pr] = x[pr], x[pl]
            pl += 1
            pr -= 1

    print(f'pivot은 {pivot} 입니다.')

    print(f'pivot 이하인 그룹 입니다.')
    print(*x[0:pl])

    if pr + 1 < pl:
        print(f'pivot과 일치하는 그룹 입니다.')
        print(*x[pr + 1:pl])

    print(f'pivot 이상인 그룹 입니다.')
    print(*x[pr + 1:n])


if __name__ == '__main__':
    print(('배열을 나눕니다.'))
    n = int(input('원소 수를 입력해주세요.: '))
    x = [None] * n

    for i in range(n):
        x[i] = int(input(f'x[{i}]: '))

    partition(x)
