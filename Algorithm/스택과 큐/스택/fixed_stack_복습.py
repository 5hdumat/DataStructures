class FixedStack:
    class FullError(Exception):
        pass

    class EmptyError(Exception):
        pass

    def __init__(self, capacity):
        self.capacity = capacity
        self.stk = [None] * capacity
        self.ptr = 0

    # 스택에 쌓여있는 데이터의 개수를 반환
    def __len__(self):
        return self.ptr

    def is_empty(self):
        return self.ptr <= 0

    def is_full(self):
        return self.ptr >= self.capacity

    def push(self, value):
        if self.is_full():
            raise FixedStack.FullError

        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self):
        if self.is_empty():
            raise FixedStack.EmptyError

        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self):
        if self.is_empty():
            raise FixedStack.EmptyError

        self.stk[self.ptr - 1]

    def find(self, value):
        for i in range(self.ptr, -1, -1):
            if self.stk[i] == value:
                return i

        else:
            return -1

    def count(self, value):
        c = 0

        for i in range(self.ptr):
            if self.stk[i] == value:
                c += 1

        return c

    def __contains__(self, value):
        return self.count(value)

    def dump(self):
        if self.is_empty():
            print('스택이 비어있습니다.')
        else:
            print(self.stk[:self.ptr])



