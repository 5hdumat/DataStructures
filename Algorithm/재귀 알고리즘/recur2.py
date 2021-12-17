'''
재귀 알고리즘의 비재귀적 구현
'''

'''
[꼬리 재귀 재거하기]

recur()의 맨 끝에서 재귀 호출하는 꼬리재귀 recur(n-2)의 의미는 '인수로 n-2의 값을 전달하고 recur() 함수를 호출하는 것' 이다.
이 작업은 'n의 값을 n-2로 업데이트하고 함수의 시작 지점으로 돌아가게 함으로써 대체할 수 있다.'
'''


def recur(n: int) -> int:
    # 인수로 n-2의 값을 전달하고 recur() 함수를 호출
    # if n > 0:
    #     recur(n - 1)
    #     print(n)
    #     recur(n - 2)

    # 인수로 n-2의 값을 전달하고 recur() 함수를 호출
    while n > 0:
        recur(n - 1)
        print(n)
        n = n - 2

n = int(input('정수를 입력해주세요.: '))
recur(n)


'''
[재귀없이 구현하기] 

p. 199 참고
꼬리 재귀와 달리 맨 앞에서 호출되는 재귀 recur(n-1)은 제거가 까다롭다. 
왜냐하면 n 값을 출력하기 전에 recur(n-1)을 실행해햐 하기 때문이다.
(n 값이 4인 경우 recur(3)을 실행한 후 4를 출력해야 하기 때문에 4를 어딘가에 저장해둬야 한다.)

이전에 만들어 두었던 스택를 활용하여 재귀없이 구현해보자.
'''

from fixed_stack import FixedStack

def recur(n):
    stk = FixedStack(n)

    while True:
        if n > 0:
            stk.push(n)
            n = n - 1
            continue

        if not stk.is_empty():
            n = stk.pop()
            print(n)
            n = n - 2
            continue

        break

n = int(input('정수를 입력해주세요.: '))
recur(n)



