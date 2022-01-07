def kmp_match(txt, pat):
    pt = 1
    pp = 0
    skip = [0] * (len(pat) + 1)

    while pt < len(pat):
        if pat[pt] == pat[pp]:
            pt += 1
            pp += 1
            skip[pt] = pp
        elif pp == 0:
            pt += 1
        else:
            print(pp)
            pp = skip[pp]
    print(skip)
    '''
    pt = 2
    pp = 1
    
    [0, 0, 0, 1, 0, 0, 1, 2, 3, 2, 3, 1, 2, 3, 2]
    
    BABDCBABABBABA
                BABDCBABABBABA
    
    t: ABDBABAB
    p:     ABAB
    '''
    pt = pp = 0
    while pt < len(txt):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        elif pp == 0:
            pt += 1
        else:
            pp = skip[pp]

    if pp == len(pat):
        return pt - pp + 1


if __name__ == '__main__':
    s1 = input('텍스트를 입력하세요.: ')
    s2 = input('패턴을 입력하세요.: ')

    idx = kmp_match(s1, s2)

    if idx == -1:
        print('텍스트 안에 패턴이 존재하지 않습니다.')
    else:
        print(f'{(idx)}번째 문자가 일치합니다.')
