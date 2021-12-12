'''
배열 원소의 최댓값을 구하는 함수 구현
'''
from typing import Any, Sequence


def max_of(a: Sequence) -> Any:
    maximum = a[0]

    for i in range(1, len(a)):
        if maximum < a[i]:
            maximum = a[i]

    return maximum

'''
재사용할 수 있는 모듈로 작성

파이썬은 하나의 스크립트 프로그램을 모듈이라고 한다. 
확장자(.py)를 포함하지 않는 파일의 이름 자체를 모듈 이름으로 사용한다.
모든 것을 객체로 다루는 파이썬에서는 모듈도 당연히 객체임, 모듈은 프로그램이 처음 임포트되는 시점에 그 모듈 객체가 생성되면서 초기화되는 구조이다.

따라서 if __name__ == '__main__': 는 모듈 객체 max.py를 직접 실행한 경우에만 참이 되어 26~ 라인을 실행할 수 있다.
(다른 스크립트 프로그램에서 임포트한 경우에는 겆시이 되므로 if문이 실행되지 않는다.)
'''
if __name__ == '__main__':
    print('배열의 최댓값을 구합니다.')
    num = int(input('원소 수를 입력해주세요.'))

    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]값을 입력하세요:'))

    print(f'최댓값은 {max_of(x)} 입니다.')
