'''
병합 정렬

배열을 앞 부분과 뒷 부붐의 두 그룹으로 나누어 각각 정렬한 후 벙합하는 잡얼을 반복하는 알고리즘

1. 배열의 앞 부분을 병합 정렬로 정렬한다.
1. 배열의 뒷 부분을 병합 정렬로 정렬한다.
1. 배열의 앞 부분과 뒷 부분을 병합한다.
'''


def merge_sort(x):
    def _merge_sort(x, left, right):
        if left < right:
            center = (left + right) // 2

            _merge_sort(x, left, center)  # 배열의 앞 부분을 병합 정렬
            _merge_sort(x, center + 1, right)  # 배열의 뒷 부분을 병합 정렬

            '''
            앞 부분과 뒷 부분 병합 과정
            '''
            bp = bk = 0  # buffer_point를 bp라고 정의했다. k는 논리 포인트
            mp = mk = left  # main_point를 mp라고 정의했다. k는 논리 포인트

            # 배열의 앞부분부터 center까지 x 원소를 buffer에 저장
            while mp <= center:
                buff[bp] = x[mp]
                bp += 1
                mp += 1

            # 배열의 center부터 n까지 buffer에 담겨진 원소와 비교해가며 x에 저장
            while mp <= right and bk < bp:
                if buff[bk] <= x[mp]:
                    x[mk] = buff[bk]
                    bk += 1
                else:
                    x[mk] = x[mp]
                    mp += 1
                mk += 1

            # 버퍼에 원소가 남아있으면 x에 이어붙이기
            while bk < bp:
                x[mk] = buff[bk]
                mk += 1
                bk += 1

    buff = [None] * n  # 작업용 배열 생성
    _merge_sort(x, 0, n - 1)  # 배열 전체를 병합 정렬
    del buff  # 작업이 완료되었으면 소멸


if __name__ == '__main__':
    n = int(input('원소 수를 입력해주세요.: '))
    x = [None] * n

    for i in range(n):
        x[i] = int(input(f'x[{i}]: '))

    merge_sort(x)

    for i in range(n):
        print(f'x[{i}] = {x[i]}')
