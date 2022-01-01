from __future__ import annotations


class Node:
    def __init__(self, data, next: Node):
        self.data = data
        self.next = next


class LinkedListIterator:
    def __init__(self, head):
        # 이터레이터 인스턴스에서만 쓰는 필드
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data


class LinkedList:
    def __init__(self):
        self.no = 0
        self.head = None
        self.current = None

    def search(self, data) -> int:
        cnt = 0
        ptr = self.head

        while ptr is not None:
            if ptr.data == data:
                self.current = ptr
                return cnt

            cnt += 1
            ptr = ptr.next

        return -1

    def __contains__(self, data):
        return self.search(data) >= 0

    def add_first(self, data):
        ptr = self.head

        if ptr is None:
            self.head = Node(data, None)
        else:
            self.head = Node(data, ptr)

        self.no += 1
        self.current = self.head

    def add_last(self, data):
        ptr = self.head

        if ptr is None:
            self.add_first(data)
        else:
            while ptr.next is not None:
                ptr = ptr.next

            ptr.next = Node(data, None)
            self.current = ptr.next
            self.no += 1

    def remove_first(self):
        if self.head is not None:
            if self.head.next is None:
                self.head = None
                self.current = None
                self.no -= 1
            else:
                self.head = self.head.next
                self.current = self.head
                self.no -= 1

    def remove_last(self):
        if self.head is not None:
            if self.head.next is None:
                self.remove_first()
            else:
                ptr = self.head
                pre = self.head

                while ptr.next is not None:
                    pre = ptr
                    ptr = ptr.next

                pre.next = None
                self.current = pre
                self.no -= 1

    def remove(self, p):
        if self.head is not None:
            if self.head.next is None:
                self.remove_first()
            else:
                ptr = self.head

                while ptr.next is not p:
                    ptr = ptr.next

                    if ptr is None:
                        return

                ptr.next = p.next
                self.current = ptr
                self.no -= 1

    def remove_current_node(self):
        self.remove(self.current)

    # 전체 노드 삭제
    def clear(self):
        while self.head is not None:
            self.remove_first()

        self.current = None
        self.no = 0

    def next(self):
        if self.current is None or self.current.next is None:
            return False
        else:
            self.current = self.current.next
            return True

    # 주목 노드 출력
    def print_current_node(self):
        if self.current is None:
            print('주목 노드가 존재하지 않습니다.')
        else:
            print(self.current.data)

    # 모든 노드를 출력
    def print(self):
        ptr = self.head

        while ptr is not None:
            print(ptr.data)
            ptr = ptr.next

    def __iter__(self):
        return LinkedListIterator(self.head)
