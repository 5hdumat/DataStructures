'''
단순 선택 정렬 (안정적이지 않은 정렬, O(n**2))

가장 작은 원소를 찾아 선택한 후 알맞은 위치로 옮기는 작업을 반복하는 정렬
'''


def selection_sort(x):
    for i in range(num - 1):
        # 가장 작은 인덱스 값 부터 시작
        min = i

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
