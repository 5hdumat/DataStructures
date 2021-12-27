'''
good suffix, bad character 고려하지않고 배열 1개로 구현

1. 패턴에 포함되지 않은 문자를 만났을 경우 패턴의 길이(len(pat)) 만큼 건너뛰기
2. 패턴에 포함된 문자를 만났을 경우 최우단이 패턴 문자와 문자 위치 맞춰주기
3. 반복되는 패턴 (ABAB와 같이) 이 아닌 상태의 패턴 ACAC가 비교 문자와 일치하지 않고, C를 만났을 경우에도 패턴의 길이(len(pat)) 만큼 건너뛰기
'''


def bm_match(txt, pat):
    skip = [None] * 256  # 문자열 유니코드 256개

    for pt in range(256):
        skip[pt] = len(pat)

    for pt in range(len(pat)):
        skip[ord(pat[pt])] = len(pat) - pt - 1

    while pt < len(txt):
        pp = len(pat) - 1

        while txt[pt] == pat[pp]:
            if pp == 0:
                return pt

            pt -= 1
            pp -= 1

        if skip[ord(pat[pt])] > len(pat) - pp:
            pt += skip[ord(pat[pt])]
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
