'''
버블 정렬: 이웃한 원소의 대소관계를 비교하여 교환하는 정렬
'''


# 기본 버블 정렬
def bubble_sort(x):
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if x[j - 1] > x[j]:
                x[j - 1], x[j] = x[j], x[j - 1]


# 버블 정렬 개선 - 1
# 특정 패스에서 더 이상 교환이 이루어지지 않으면 반복문 종료
def bubble_sort2(x):
    for i in range(n - 1):
        exchange = 0
        for j in range(n - 1, i, -1):
            if x[j - 1] > x[j]:
                x[j - 1], x[j] = x[j], x[j - 1]
                exchange += 1

        if exchange == 0:
            break


# 버블 정렬 개선 - 2
# 마지막으로 정렬된 원소의 위치를 기억해둔 후 다음 정렬 때 마지막으로 정렬된 원소의 위치까지만 정렬을 수행
def bubble_sort3(x):
    k = 0
    while k < n - 1:
        last = n - 1

        # 3개가 교환되었다면 j는 0->1->2로 2가 반환될 것이고, 이는 곧 마지막으로 교환한 위치이다.
        # 이를 기억해두기 위해 k에 저장한다.
        # 더 이상 교환이 이루어지지 않으면 위에 선언된 last(n - 1)이 그대로 반환되고, while문을 빠져나오게 된다.
        for j in range(i, k, -1):
            if x[j - 1] > x[j]:
                x[j - 1], x[j] = x[j], x[j - 1]
                last = j

        k = last


def shaker_sort(x):
    left = 0
    right = n - 1
    last = right
    while left < right:
        # 홀수 패스(뒤에서 부터 스캔하며 작은 원소를 앞으로 옮김)
        for j in range(right, left, -1):
            if x[j - 1] > x[j]:
                x[j - 1], x[j] = x[j], x[j - 1]
                last = j

        # 1
        left = last

        # 짝수 패스(앞에서 부터 스캔하여 큰 원소를 뒤로 옮김)
        for j in range(left, right):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
                last = j

        # 5
        right = last


if __name__ == '__main__':
    n = int(input('원소의 개수를 입력하세요: '))
    x = [None] * n

    for i in range(n):
        x[i] = int(input(f'x[{i}]: '))

    shaker_sort(x)

    print(x)
