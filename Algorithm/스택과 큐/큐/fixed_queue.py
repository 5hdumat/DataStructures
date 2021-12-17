from typing import Any


class FixedQueue:
    class EmptyError(Exception):
        pass

    class FullError(Exception):
        pass

    def __init__(self, capacity: int) -> None:
        # 큐에 쌓여있는 데이터 개수를 나타내는 정수.
        # 원소의 Enqueue와 dequeue를 반복하다보면 front와 rear가 같아지는 시점이 있는데 이 때 큐가 가득찬건지, 비어있는건지 판단하기위해 필요하다.
        self.no = 0
        self.front = 0  # 맨 앞 원소의 커서
        self.rear = 0  # 맨 뒤 원소의 커서
        self.capacity = capacity  # 큐 용량
        self.que = [None] * self.capacity  # 큐도 배열로 구현

    def __len__(self):
        return self.no

    def is_empty(self):
        return self.no <= 0

    def is_full(self):
        return self.no >= self.capacity

    # 데이터를 넣는 함수 Enqueue
    def enqueue(self, value: Any) -> Any:
        if self.is_full():
            raise FixedQueue.FullError

        self.que[self.rear] = value
        self.rear += 1
        self.no += 1

        # rear의 값을 1 증가시켰는데 큐 용량의 한계를 넘어버리면 다시 rear 값을 0으로 되돌린다.
        # 이렇게 되면 도넛 모양의 링 버퍼 형태가 된다.
        if self.rear == self.capacity:
            self.rear = 0

    # 데이터를 꺼내는 함수 Dequeue
    def dequeue(self):
        if self.is_empty():
            raise FixedQueue.EmptyError

        x = self.que[self.front] # 큐의 맨 앞부터 데이터를 디큐하여 그 값을 반환

        self.front += 1 # 반환 후 front를 1 증가시켜주고
        self.no -= 1 # 데이터를 반환했으니 큐에 담긴 데이터 개수 -1을 해준다.

        # front값이 증가하다가 큐의 용량을 넘어서게되면 0으로 다시 되돌린다.
        if self.front == self.capacity:
            self.front = 0

        return x

    # 데이터를 들여다보는 peek 함수 (readOnly, 맨 앞자리 반환)
    def peek(self):
        if self.is_empty():
            raise FixedQueue.EmptyError

        return self.que[self.front]

    # 데이터 인덱스 찾기
    def find(self, value: Any) -> Any:
        for i in range(self.no): # 큐에 들어있는 원소 만큼 반복문 돌리기 (주의해야할 점은 큐의 인덱스 0 부터가 아닌 데이터가 들어있는 부분 부터 돌려야 한다.)
            index = (i + self.front) % self.capacity
            if self.que[index] == value:
                return index

        return -1

    # 데이터 개수 찾기
    def count(self, value):
        c = 0

        for i in range(self.no): # 큐에 들어있는 원소 만큼 반복문 돌리기 (주의해야할 점은 큐의 인덱스 0 부터가 아닌 데이터가 들어있는 부분 부터 돌려야 한다.)
            index = (i + self.front) % self.capacity
            if self.que[index] == value:
                c += 1

        return c

    def clear(self):
        self.front = 0
        self.rear = 0
        self.no = 0

    def __contains__(self, value):
        return self.count(value)

    def dump(self):
        if self.is_empty():
            print('큐가 비어있습니다.')
        else:
            for i in range(self.no):
                index = (i + self.front) % self.capacity

                print(self.que[index], end=' ')
            print()


