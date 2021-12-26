import heapq


def heap_sort(x):
    heap = []

    for i in x:
        heapq.heappush(heap, i)

    return heap


if __name__ == '__main__':
    n = int(input('원소 수를 입력하세요: '))
    x = [None] * n

    for i in range(n):
        x[i] = int(input(f'x[{i}]: '))

    heap = heap_sort(x)

    for i in range(n):
        print(f'x[{i}] = {heapq.heappop(heap)}')
