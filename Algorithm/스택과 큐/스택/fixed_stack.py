'''
stack : 데이터를 임시 저장하기 위한 자료구조, 후입선출(LIFO)

'''
from collections import deque
from typing import Any


'''
파이썬에서 시작과 끝에 언더스코어(__)가 붙은 함수는 특별한 의미가 있다. (__function__을 던더 함수라고 한다.)
__len__() 함수를 정의하면 클래스형 인스턴스를 len()함수에 전달할 수 있다.

FixedStack.__len()__ 과 같이 함수를 호출해야하는데 간단히 len(FixedStack)으로 작성 가능하다.
__contain__ 은 x in FixedStack과 같이 작성 가능하다.
'''
class FixedStack:
    '''
    예외처리 클래스 Empty, full
    -> 스택이 비어 있거나 가득 차있으면 내보낸다(pass).

    참고로 파이썬은 프로그래머가 정의하는 사용자 정의 예외처리는 Exception에서 파생하는 것을 원칙으로 한다.

    https://docs.python.org/ko/3/tutorial/errors.html#tut-userexceptions
    내장 예외 클래스는 새 예외를 정의하기 위해 서브 클래싱 될 수 있습니다.
    BaseException 이 아니라 Exception 클래스 나 그 서브 클래스 중 하나에서 새로운 예외를 파생시킬 것을 권장합니다. 예외 정의에 대한 더 많은 정보는 파이썬 자습서의 사용자 정의 예외 에 있습니다.
    '''
    class EmptyError(Exception):
        pass

    class FullError(Exception):
        pass

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity  # 스택의 크기
        self.stk = [None] * self.capacity  # 스택은 배열로 구현
        self.ptr = 0  # 스택 포인터

    # 스택에 쌓여 있는 데이터의 개수를 알아내는 함수
    def __len__(self) -> int:
        return self.ptr  # 포인터의 위치를 그대로 반환하면 된다.

    # 스택이 비어 있는지 체크한다.
    def is_empty(self) -> bool:
        return self.ptr <= 0

    # 스택이 꽉 차있는지 체크한다.
    def is_full(self) -> bool:
        return self.ptr >= self.capacity

    def push(self, value: Any) -> None:
        if self.is_full():  # 스택이 가득 차있는가?
            raise FixedStack.Full  # 예외처리

        # 스택이 가득 차 있지 않으면 전달받은 value를 스택에 저장하고 스택 포인터를 1 증가시킨다.
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> Any:
        if self.is_empty():  # 스택이 비어있는가?
            raise FixedStack.Empty  # 예외처리

        self.ptr -= 1
        return self.stk[self.ptr]

    # 스택 꼭대기 들여다보기 (readOnly, 스택 포인터에 따로 변화를 주지 X)
    def peek(self) -> Any:
        if self.is_empty():  # 스택이 비어있는가?
            raise FixedStack.Empty  # 예외처리

        return self.stk[self.ptr - 1]

    def clear(self):
        self.ptr = 0

    # 스택에서 데이터 찾기
    def find(self, value: Any) -> Any:
        for i in range(self.ptr, -1, -1):  # self.ptr 부터 0까지 거꾸로 선형 탐색
            if self.stk[i] == value:
                return i

        return -1  # 찾고자 하는 데이터가 없음

    # 스택에 담겨있는 value의 개수 확인
    def count(self, value: Any) -> int:
        c = 0

        for i in range(self.ptr):  # self.ptr 부터 0까지 거꾸로 선형 탐색
            if self.stk[i] == value:
                c += 1

        return c

    # 찾고자 하는 데이터가 스택에 존재(포함)하는지 체크
    def __contains__(self, value: Any) -> bool:
        return self.count(value) > 0

    # 스택의 모든 데이터 출력
    def dump(self):
        if self.is_empty():
            print('스택이 비어있습니다.')
        else:
            print(self.stk[:self.ptr])


'''
파이썬 deque를 사용하여 고정 길이 스택 구현하기
'''


class Stack:

    def __init__(self, capacity: int = 256) -> None:
        # maxlen 속성은 deque의 최대 크기를 나타내는 속성으로 읽기 전용이다.
        # 크기 제한이 없으면 None
        self.capacity = capacity
        self.__stk = deque([], maxlen=self.capacity)

    def __len__(self):
        return len(self.__stk)

    def is_full(self):
        return len(self.__stk) == self.__stk.maxlen

    def is_empty(self):
        return not self.__stk

    def push(self, value):
        self.__stk.append(value)

    def pop(self):
        return self.__stk.pop()

    def peek(self):
        return self.__stk[-1]

    def clear(self):
        self.__stk.clear()

    def find(self, value):
        # 스택에서 value를 찾아 인덱스를 반환. 찾지 못하면 -1을 반환해준다.
        try:
            return self.__stk.index(value)
        except ValueError:
            return -1

    def __contains__(self, value):
        return self.__stk.count(value)

    def dump(self):
        print(list(self.__stk))


