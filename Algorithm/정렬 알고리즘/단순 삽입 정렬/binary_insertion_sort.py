'''
이진 삽입 정렬

이진 검색을 활용하여 삽입 정렬을 진행하면 원소의 수가 많아도 이미 정렬을 마친 배열을 제외하고 원소를 삽입해야 할 위치를 검사하므로 비용을 크게 줄일 수 있다.
이진 삽입 정렬은 i 값에 따라 i 이전 값은 정렬됐다는 가정을 하고 시작해야한다.

1. x= [1, 1, 3, 2, 3, 1] 에 i가 3이면 x의 0번째부터 2번째까지는 이미 삽입 정렬이 끝났다는 의미이다. i 이후 원소에 더 작은값이 있든 없든 그건 일단 신경쓰지 않는다.

2. 이후 x의 인덱스 값을 구한다.

pl     pr
[1, 1, 3]

고로 pl = 0, pr = 2이다. pc는 (pl + pr) // 2 이므로 1이다.

3. 다음으로 pc와 비교 대상인 x[i] 즉 x[3](2) 값과 비교한다.
x[pc] 즉, x[1]의 값은 1이므로 x[i] 보다 작다. 그러므로 pc 이전의 값은 더 이상 탐색하지 않아도 된다.(이미 정렬되었으니 말이다.)

4. pl 을 pc + 1 해준다.
이제 pl = 2, pr = 2가 되었다.

5. pc를 다시 구해준다. (2 + 2) // 2 이므로 pc = 2 이다.

6. x[2]의 원소와 x[3]의 원소를 비교했을 때 더 크므로, 이제는 pr을 -1 해준다.

7. pr = 1로 변경되었으나 pr이 pl보다 더 작아졌으므로 반복문이 종료된다.

8. 이제 pr과 pl을 비교한다.
pr이 더 작아졌다는 의미는 정렬된 원소 중 삽입해야 할 원소보다 더 큰 값이 존재한다는 의미이며, pl이 pr보다 작거나 같다는 것은 정렬된 원소 중 동일한 원소 혹은 더 작은 원소가 존재한다는 의미이다.

그러므로 아래와 같은 식을 구해준다.

if pl <= pr:
    pd = pc + 1
else:
    pd = pr + 1

9. 다음으로 원소 i부터 pd 까지 반복문을 돌리며, 삽입해야할 원소 뒤 원소들은 밀어주고 그 자리에 본인을 삽입한다.
for j in range(i, pd, -1):
    x[j] = x[j - 1]
x[pd] = x[i]
'''

import bisect

# pc = 1
# 0 1 2 3

# 1 2 3 4 1
def binary_insertion_sort(x):
    for i in range(1, n):
        key = x[i]
        pl = 0
        pr = i - 1

        while True:
            pc = (pl + pr) // 2

            if x[pc] == key:
                break
            elif x[pc] < key:
                pl = pc + 1
            else:
                pr = pc - 1

            if pl > pr:
                break

        pd = pc + 1 if pl <= pr else pr + 1

        for j in range(i, pd, -1):
            x[j] = x[j - 1]

        x[pd] = key

# 파이썬 응용
def binary_insertion_sort_python(x):
    for i in range(1, n):
        '''
        bisect.insert(a, x, lo, hi)
        
        a 배열의 정렬 상태를 유지하면서 lo, hi 사이에 x를 삽입한다.
        동일한 원소가 존재한다면 가장 오른쪽 위치에 삽입한다.
        '''

        bisect.insort(x, x.pop(i), 0, i)

if __name__ == '__main__':
    n = int(input('원소의 개수를 입력하세요: '))
    x = [None] * n

    for i in range(n):
        x[i] = int(input(f'x[{i}]: '))

    binary_insertion_sort(x)

    print(x)
