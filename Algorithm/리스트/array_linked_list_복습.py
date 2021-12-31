Null = -1


class Node:
    def __init__(self, data=Null, next=Null, dnext=Null):
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
        if self.current == Null:
            raise StopIteration
        else:
            data = self.current
            self.current = self.n[self.current].next
            return data


class ArrayLinkedList:
    def __init__(self, capacity):
        self.head = Null
        self.current = Null
        self.max = Null
        self.deleted = Null
        self.capacity = capacity
        self.n = [Node()] * self.capacity
        self.no = 0

    def __len__(self):
        return self.no

    # 삽입 할 인덱스 구하기
    def get_insert_index(self):
        # 삭제된 노드가 없다면
        if self.deleted == Null:
            if self.max + 1 < self.capacity:
                self.max += 1
                return self.max
            else:
                return Null
        else:
            rec = self.deleted
            self.deleted = self.n[rec].dnext
            return rec

    # 프리 리스트에 레코드 등록
    def delete_index(self, idx):
        if self.deleted == Null:
            self.deleted = idx
            self.n[idx].dnext = Null
        else:
            rec = self.deleted
            self.deleted = idx
            self.n[idx].dnext = rec

    # 데이터 검색
    def search(self, data) -> int:
        cnt = 0
        ptr = self.head

        while ptr != Null:
            if self.n[ptr].data == data:
                self.current
                return cnt

            cnt += 1
            ptr = self.n[ptr].next

        return -1

    def __contains__(self, data):
        return self.search(data) >= 0

    def add_first(self, data):
        ptr = self.head
        rec = self.get_insert_index()

        if rec != Null:
            self.head = self.current = rec
            self.n[rec] = Node(data, ptr)
            self.no += 1

    def add_last(self, data):
        if self.head == Null:
            self.add_first(data)

        else:
            ptr = self.head

            while self.n[ptr].next != Null:
                ptr = self.n[ptr].next

            rec = self.get_insert_index()

            if rec != Null:
                self.n[ptr].next = self.current = rec
                self.n[rec] = Node(data)
                self.no += 1

    def remove_first(self):
        if self.head != Null:
            ptr = self.n[self.head].next
            self.delete_index(ptr)
            self.head = self.current = ptr
            self.no -= 1

    def remove_last(self):
        if self.head != Null:
            if self.n[self.head].next == Null:
                self.remove_first()
            else:
                pre = self.head
                ptr = self.head

                while self.n[ptr].next != Null:
                    pre = ptr
                    ptr = self.n[ptr].next

                self.delete_index(ptr)
                self.n[pre].next = Null
                self.current = pre
                self.no -= 1

    # 특정 레코드 삭제
    def remove(self, p):
        if self.head != Null:
            if self.n[self.head].data == p:
                self.remove_first()
            else:
                ptr = self.head

                while self.n[ptr].data != p:
                    ptr = self.n[ptr].next

                    if ptr == Null:
                        return

                self.delete_index(p)
                self.n[ptr] = self.n[p].next
                self.current = ptr
                self.no -= 1

    # 주목 노드 삭제
    def remove_current_node(self):
        return self.remove(self.current)

    def clear(self):
        while self.head != Null:
            self.remove_first()

        self.current = Null

    def next(self) -> bool:
        if self.current == Null or self.n[self.current].next == Null:
            return False
        else:
            self.current = self.n[self.current].next
            return True

        # 주목 노드 출력

    def print_current_node(self):
        if self.current == Null:
            print('주목 노드가 없습니다.')
        else:
            print(self.n[self.current].data)

    def print(self):
        ptr = self.head

        while ptr != Null:
            print(self.n[ptr].data)
            ptr = self.n[ptr].next

    def dump(self):
        for i in self.n:
            print(f'[{i}] {i.data} {i.next} {i.dnext}')

    def __iter__(self):
        return ArrayLinkedListIterator(self.n, self.head)
