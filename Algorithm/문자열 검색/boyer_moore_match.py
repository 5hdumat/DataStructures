'''
보이어-무어법

보이어무어법은 평균적으로 KMP법보다 더 효율적이어서 실제 문자열 검색에서 널리 쓰이는 알고리즘이다.(워드프로세서의 문자열 검색이 보이어 무어로 구현)

보이어 무어법은 패턴을 앞쪽부터 검사하는게 아닌 뒷쪽부터 검사하면서 앞을향해 나아간다. 이 과정에서 일치하지 않는 문자를 발견하면 미리 준비한 건너뛰기 표를 바탕으로
패턴이 이동하는 값을 결정한다.

건너뛰기 표 조건은 2가지로 나뉜다. (패턴의 길이 = n)

- 패턴에 포함되지 않는 문자를 만난 경우
패턴을 패턴의 길이 n 만큼 이동시킨다.

- 패턴에 포함되는 문자를 만난 경우.
 1. 패턴의 마지막 검사 인덱스가 k이면 이동량은 'n - k -1'이다.
 2. 패턴안에 중복되는 문자(ABCABC와 같은)가 존재하지 않으면 패턴의 이동량은 n이다.

단점으로는 최악의 경우 시간복잡도가 n(NM)이라는 점이다. (알고리즘의 외부 루프가 len(txt)만큼 반복되고, 내부 루프가 len(pat)-1만큼 반복되는 케이스)

'''


def bm_match(txt, pat):
    pt_len = len(pat)
    skip = [pt_len] * 256

    for pt in range(len(pat)):
        skip[ord(pat[pt])] = len(pat) - pt - 1  # 패턴 이동 공식: n - k - 1

    while pt < len(txt):
        pp = len(pat) - 1

        while txt[pt] == pat[pp]:
            if pp == 0:
                return pt

            pt -= 1
            pp -= 1

        if skip[ord(txt[pt])] > len(pat) - pp:
            pt += skip[ord(txt[pt])]
        else:
            pt += len(pat) - pp

    return -1


if __name__ == '__main__':
    s1 = input('텍스트를 입력하세요.: ')
    s2 = input('패턴을 입력하세요.: ')

    idx = bm_match(s1, s2)

    if idx == -1:
        print('텍스트 안에 패턴이 존재하지 않습니다.')
    else:
        print(f'{(idx)}번째 문자가 일치합니다.')
