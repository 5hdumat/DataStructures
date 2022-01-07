'''
힙 정렬은 힙의 특성을 이용하여 정렬하는 알고리즘.
힙(heap)은 부모의 값이 자식의 값보다 항상 크다. 혹은 부모의 값이 자식의 값보다 항상 작다와 같은 조건을 만족하는 완전 이진 트리이다.
즉, 부모와 자식 두 값의 대소 관계가 항상 일정하면 된다. 그렇기 때문에 최댓값 혹은 최솟값은 항상 루트에 위치한다. 이러한 특징을 이용하여 정렬하는 알고리즘이다.


[특징]
힙은 부모와 자식의 관계는 항상 일정하지만 형제 노드끼리의 대소 관계까 저해져 있지 않아 '부분 순서 트리(partial ordered tree)'라고도 한다.

힙의 원소 배열은 가장 위쪽에서부터 한 단계 아래씩 인덱스 값을 1씩 증가시키면서 각 원소를 저장한다. (왼쪽에서 오른쪽으로)
                                        10
                                  9            5
                             8        3    2       4
                          6    7   8

                      arr = [10, 9, 5, 8, 3, 2 , 4, 6, 7, 8]

이러한 순서대로 힙을 배열에 저장하면 부모 인덱스와 아래에 있는 자식(왼쪽 자식), 오른쪽 아래에 있는 자식(오른쪽 자식) 인덱스 사이에는 다음과 같은 관계가 성립한다.

부모 원소 arr[i]에서
- 부모: a[(i - 1) // 2]
- 왼쪽 자식: a[i * 2 + 1]
- 오른쪽 자식: a[i * 2 + 2]
'''


def heap_sort(x):
    def down_heap(x, left, right):
        temp = x[left]

        parent = left
        # parent가 2로 들어왔는데 (전체 원소 // 2) 가
        # parent보다 작거나 같다는 것은 parent는 자식이 없다는 의미
        while parent < (right + 1) // 2:
            cl = parent * 2 + 1  # 왼쪽 자식 노드
            cr = parent * 2 + 2  # 오른쪽 자식 노드

            # 오른쪽 자식과 왼쪽 자식을 비교하여 큰 값을 선택,
            # 왼쪽 자식 노드만 있다면 cr <= right 조건에 의해 왼쪽 자식노드만 선택된다.
            if cr <= right and x[cr] > x[cl]:
                child = cr
            else:
                child = cl

            # 부모 노드보다 큰 자식노드가 없다면 반복문 종료 (가장 하단의 자식 노드부터 힙을 만들면서 바텀업으로 올라가기 때문에 적용 가능한 조건)
            if temp >= x[child]:
                break

            x[parent] = x[child]
            parent = child

        x[parent] = temp

    # n = 5를 기준으로 (n - 1) // 2를하면 2부터 역순으로 1, 0이 된다.  잘 생각보면 오른쪽 자식 노드부터 왼쪽 자식노드 그리고 부모노드를 가리킨다.
    for i in range((n - 1) // 2, -1, -1):
        down_heap(x, i, n - 1)

    for i in range(n - 1, 0, -1):
        # 배열 뒤에 정렬된 최대값 루트를 하나씩 삽입한다.
        print(x[0], x[i])
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
