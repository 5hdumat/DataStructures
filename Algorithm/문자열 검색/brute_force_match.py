'''
브루트 포스법

문자열 검색에서 가장 기초적이고 단순한 알고리즘으로 선형 검색에서 단순하게 확장한 알고리즘 기법이다. (단순법이라고도 한다.)
브루투 포스는 이미 검사한 위치를 기억하지 못하므로 효율이 좋지 않다.
'''
def bf_match(txt, pat):
    pt = pp = 0

    while pt < len(txt) and pp < len(pat):
        if txt[pt] == txt[pp]:
            pt += 1
            pp += 1
        else:
            pt = pt - pp + 1
            pp = 0

    if pp == len(pat):
        return pt - pp + 1
    else:
        return -1


if __name__ == '__main__':
    s1 = input('텍스트를 입력하세요.: ')
    s2 = input('패턴을 입력하세요.: ')

    idx = bf_match(s1, s2)

    if idx == -1:
        print('텍스트 안에 패턴이 존재하지 않습니다.')
    else:
        print(f'{(idx)}번째 문자가 일치합니다.')
