'''
단순 삽입 정렬 (shuttle sort, O(n**2))

주목한 원소보다 더 앞쪽에 알맞은 위치가 존재하면 삽입하는 정렬 알고리즘이다.
단순 정렬과 비슷해보이지만 가장 작은 원소를 선택해 정렬하지 않는다는 점이 다르다.
'''

def insertion_sort(x):
    for i in range(1, n):
        j = i
        key = x[i]

        while j > 0 and x[j - 1] > key:
            x[j] = x[j - 1]
            j -= 1

        x[j] = key


if __name__ == '__main__':
    n = int(input('원소의 개수를 입력하세요: '))
    x = [None] * n

    for i in range(n):
        x[i] = int(input(f'x[{i}]: '))

    insertion_sort(x)

    print(x)
