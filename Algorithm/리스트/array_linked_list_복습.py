class Node:
    def __init__(self, data=None, next=None, dnext=None):
        self.data = data
        self.next = next
        self.dnext = dnext


class ArrayLinkedListIterator:
    def __init__(self, n, head):
        self.n = n
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            data = self.current
            self.current = self.n[self.current].next
            return data


class ArrayLinkedList:
    def __init__(self, capacity):
        self.head = None
        self.current = None
        self.deleted = None
        self.max = -1
        self.capacity = capacity
        self.n = [Node()] * self.capacity
        self.no = 0

    def __len__(self):
        return self.no

    def get_insert_index(self) -> int:
        if self.deleted is None:
            if self.max < self.capacity:
                self.max += 1
                return self.max
            else:
                return -1
        else:
            rec = self.deleted
            self.deleted = self.n[rec].next
            return rec

    def delete_index(self, idx):
        if self.deleted is None:
            self.deleted = idx
            self.n[idx].dnext = None
        else:
            rec = self.deleted
            self.deleted = idx
            self.n[self.deleted].dnext = rec

    def search(self, data) -> int:
        cnt = 0
        ptr = self.head

        while ptr is not None:
            if self.n[ptr].data == data:
                self.current = ptr
                return cnt

            cnt += 1
            ptr = self.n[ptr].next

        return -1

    def __contains__(self, data):
        return self.search(data) >= 0

    def add_first(self, data):
        ptr = self.head
        rec = self.get_insert_index()

        if rec != -1:
            self.n[rec] = Node(data, ptr)
            self.head = self.current = rec
            self.no += 1

    def add_last(self, data):
        ptr = self.head

        if ptr is None:
            self.add_first(data)
        else:
            while self.n[ptr].next is not None:
                ptr = self.n[ptr].next

            rec = self.get_insert_index()

            if rec != -1:
                self.n[ptr].next = self.current = rec
                self.n[rec] = Node(data)
                self.no += 1

    def remove_first(self):
        if self.head is not None:
            ptr = self.n[self.head].next
            self.delete_index(self.head)
            self.head = self.current = ptr
            self.no -= 1

    def remove_last(self):
        if self.n[self.head].next is None:
            self.remove_first()
        else:
            ptr = self.head
            pre = self.head

            while self.n[ptr].next is not None:
                pre = ptr
                ptr = self.n[ptr].next

            self.n[pre].next = None
            self.current = pre
            self.no -= 1

    def remove(self, p):
        if self.head is not None:
            if p == self.head:
                self.remove_first()
            else:
                ptr = self.head

                while self.n[ptr].next != p:
                    ptr = self.n[ptr].next

                self.delete_index(p)
                self.n[ptr].next = self.n[p].next
                self.current = ptr
                self.no = 0

    def remove_current_node(self):
        self.remove(self.current)

    def clear(self):
        while self.head is not None:
            self.remove_first()
        self.current is None

    def next(self) -> bool:
        if self.current is None or self.n[self.current].next is None:
            return False

        self.current = self.n[self.current].next
        return True

    # 주목 노드 출력
    def print_current_node(self):
        if self.current is None:
            print('주목 노드가 없습니다.')
        else:
            print(self.n[self.current].data)

    def print(self):
        ptr = self.head

        while ptr is not None:
            print(self.n[ptr].data)
            ptr = self.n[ptr].next

    def dump(self):
        for i in self.n:
            print(f'[{i}] {i.data} {i.next} {i.dnext}')

    def __iter__(self):
        return ArrayLinkedListIterator(self.n, self.head)
