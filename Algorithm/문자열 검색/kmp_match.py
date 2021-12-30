'''
KMP법

브루트포스의 치명적인 단점은 일치하지 않운 텍스트를 만나면 이전에 검사했던 결과는 버리고 다시 패턴의 첫 문자부터 검사를 순차적으로 수행한다.
이와 달리 KMP 법은 검사한 결과를 기억해뒀다가 건너뛰기를 하면서 효율적으로 문자를 매칭할 수 있는 알고리즘이다.

KMP 법은 텍스트와 패턴안에서 겹치는 문자열을 찾아내 문자열 매칭에 실패했어도 다시 시작할 위치를 구하여 패턴의 이동(이하 건너뛰기)을 되도록이면 크게 크게 하는 알고리즘이다.

단점으로는 처리하기 복잡하고 '패턴안에 반복이 없으면 효율이 좋지 않다.'
'''
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
            pp = skip[pp]

    pt = pp = 0
    while pt < len(txt) and pp < len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        elif pp == 0:
            pt += 1
        else:
            pp = skip[pp]

    if pp == len(pat):
        return pt - pp + 1
    else:
        return -1


if __name__ == '__main__':
    s1 = input('텍스트를 입력하세요.: ')
    s2 = input('패턴을 입력하세요.: ')

    idx = kmp_match(s1, s2)

    if idx == -1:
        print('텍스트 안에 패턴이 존재하지 않습니다.')
    else:
        print(f'{(idx)}번째 문자가 일치합니다.')
