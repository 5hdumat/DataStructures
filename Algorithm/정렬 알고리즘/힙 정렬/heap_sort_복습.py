'''
                                        10
                                  9            5
                             8        3    2       4
                          6    7   8

                      arr = [10, 9, 5, 8, 3, 2 , 4, 6, 7, 8]
'''


def heap_sort(x):
    def down_heap(x, left, right):
        tmp = x[left]
        parent = left

        # parent값이 부모 노드의 갯수보다 많거나 같으면 해당 parent는 자식 노드가 없다고 판단
        while parent < (right + 1) // 2:
            cl = (parent * 2) + 1
            cr = (parent * 2) + 2

            if cr > right or x[cl] > x[cr]:
                child = cl
            else:
                child = cr

            if tmp >= x[child]:
                break

            x[parent] = x[child]
            parent = child

        x[parent] = tmp

    '''
    일단 배열이 입력되면 최댓값을 가진 루트를 도출하기 위해 힙 정렬을 수행한다.
    (트리의 최하단에 있는 오른쪽 부모 노드부터 순차적으로 힙 정렬 수행)
    '''
    for i in range((n - 1) // 2, -1, -1):
        down_heap(x, i, n - 1)

    for i in range(n - 1, 0, -1):
        x[0], x[i] = x[i], x[0]
        down_heap(x, 0, i - 1)


if __name__ == '__main__':
    n = int(input('원소 수를 입력하세요: '))
    x = [None] * n

    for i in range(n):
        x[i] = int(input(f'x[{i}]: '))

    heap_sort(x)

    for i in range(n):
        print(f'x[{i}] = {x[i]}')
