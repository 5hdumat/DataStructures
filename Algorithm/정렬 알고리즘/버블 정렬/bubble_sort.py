'''
버블 정렬 (안정적인 정렬 , O(n**2))

이웃한 두 원소의 대소 관계를 비교하여 필요에 따라 '교환'을 반복하는 알고리즘, 단순 교환 정렬이라고도 한다.

6 4 3 7 1 (9 8)
6 4 3 7 1 (8 9)
6 4 3 7 (1 8) 9
6 4 3 (7 1) 8 9
6 4 3 (1 7) 8 9
...
'''


def bubble_sort(x):
    ccnt = 0
    scnt = 0

    for i in range(num - 1):
        for j in range(num - 1, i, - 1):
            # # 정렬 과정을 출력하기 위한 반복문
            # for m in range(num):
            #     # if m != j - 1가 참이면 공백
            #     # 거짓이면 ' +' if x[j - 1] > x[j] else ' -' 실행
            #     print(f'{x[m]:2}' + (' ' if m != j - 1 else ' +' if x[j - 1] > x[j] else ' -'), end='')
            #
            # print()

            ccnt += 1
            if x[j - 1] > x[j]:
                scnt += 1
                x[j], x[j - 1] = x[j - 1], x[j]

    print(f'비교 연산은 [{ccnt}] 번, 교환 연산은 [{scnt}] 번 이루졌습니다.')


''' 
가지치기 1

패스가 하나라도 0이 나오면 (exchange가 0이면 끝에서부터 하나씩 정렬해왔는데 전혀 정렬할 게 없다는 의미) 
더 이상 확인할 필요 없이 완벽히 정렬된 상태이므로 그냥 반복문을 종료한다.
'''


def bubble_sort_cutedge1(x):
    ccnt = 0
    scnt = 0

    for i in range(num - 1):
        print(f'패스 {i + 1}')

        exchange = 0
        for j in range(num - 1, i, -1):

            # # 정렬 과정을 출력하기 위한 반복문
            # for m in range(num):
            #     # if m != j - 1가 참이면 공백
            #     # 거짓이면 ' +' if x[j - 1] > x[j] else ' -' 실행
            #     print(f'{x[m]:2}' + (' ' if m != j - 1 else ' +' if x[j - 1] > x[j] else ' -'), end='')
            #
            # print()

            ccnt += 1
            if x[j - 1] > x[j]:
                scnt += 1
                exchange += 1
                x[j], x[j - 1] = x[j - 1], x[j]

        if exchange == 0:
            break

    print(f'비교 연산은 [{ccnt}] 번, 교환 연산은 [{scnt}] 번 이루졌습니다.')


''' 
가지치기 2

뒤에서 부터 특정 자릿수 까지 정렬이 이루어진 다음부터 아무런 작업이 없었다면
다음 패스부터는 마지막으로 정렬이 이루어진 자릿수까지만 정렬한다.

'''


def bubble_sort_cutedge2(x):
    ccnt = 0
    scnt = 0

    k = 0
    i = 0
    while k < num - 1:
        print(f'패스 {i + 1}')
        last = num - 1

        # 하나씩 줄어드는 반복문임을 유의하자.
        for j in range(num - 1, k, -1):

            # # 정렬 과정을 출력하기 위한 반복문
            # for m in range(num):
            #     # if m != j - 1가 참이면 공백
            #     # 거짓이면 ' +' if x[j - 1] > x[j] else ' -' 실행
            #     print(f'{x[m]:2}' + (' ' if m != j - 1 else ' +' if x[j - 1] > x[j] else ' -'), end='')
            #
            # print()

            ccnt += 1
            if x[j - 1] > x[j]:
                scnt += 1
                x[j - 1], x[j] = x[j], x[j - 1]
                last = j

        k = last
        i += 1

    print(f'비교 연산은 [{ccnt}] 번, 교환 연산은 [{scnt}] 번 이루졌습니다.')


if __name__ == '__main__':
    num = int(input('원소의 개수를 입력하세요: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    bubble_sort_cutedge2(x)

    print(x)
