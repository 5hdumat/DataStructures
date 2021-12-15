class FixedQueue:
    class FullError(Exception):
        pass

    class EmptyError(Exception):
        pass

    def __init__(self, capacity):
        self.no = 0
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.que = [None] * self.capacity

    def __len__(self):
        return self.no

    def is_empty(self):
        return self.no <= 0

    def is_full(self):
        return self.no >= self.capacity

    def enqueue(self, value):
        if self.is_full():
            raise FixedQueue.FullError

        self.que[self.rear] = value
        self.rear += 1
        self.no += 1

        if self.rear >= self.capacity:
            self.rear = 0

    def dequeue(self):
        if self.is_empty():
            raise FixedQueue.EmptyError

        x = self.que[self.front]
        self.front += 1
        self.no -= 1

        if self.front >= self.capacity:
            self.front = 0

        return x

    def find(self, value):
        for i in range(self.no):
            index = (i + self.front) % self.capacity
            if self.que[index] == value:
                return index

        return -1

    def count(self, value):
        c = 0
        for i in range(self.no):
            index = (i + self.front) % self.capacity
            if self.que[index] == value:
                c += 1

        return c

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
