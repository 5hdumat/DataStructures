class Node():
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedListIterator:
    def __init__(self, head):
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

    def search(self, data):
        ptr = self.head
        cnt = 0

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
        self.head = self.current = Node(data, ptr)
        self.no += 1

    def add_last(self, data):
        ptr = self.head

        if ptr is None:
            self.add_first(data)
        else:
            while ptr.next is not None:
                ptr = ptr.next

            ptr.next = self.current = Node(data, None)
            self.no += 1

    def remove_first(self):
        if self.head is not None:
            self.head = self.current = self.head.next
            self.no -= 1

    def remove_last(self):
        if self.head is not None:
            if self.head.next is None:
                self.remove_first()
            else:
                pre = self.head
                ptr = self.head

                while ptr.next is not None:
                    pre = ptr
                    ptr = ptr.next

                pre.next = None
                self.current = pre
                self.no -= 1

    def remove(self, node):
        if self.head is not None:
            if node is self.head:
                self.remove_first()
            else:
                ptr = self.head

                while ptr is not node:
                    ptr = ptr.next

                    if ptr is None:
                        return

                ptr.next = node.next
                self.current = ptr
                self.no -= 1

    def remove_current_node(self):
        self.remove(self.current)

    def clear(self):
        while self.head is not None:
            self.remove_first

        self.no = 0
        self.current = None

    def print(self):
        ptr = self.head

        while ptr is not None:
            print(ptr.data)
            ptr = ptr.next

    def print_current_node(self):
        if self.current is None:
            print('주목 노드가 존재하지 않습니다.')
        else:
            print(self.current.data)

    def next(self):
        if self.current is None or self.current.next is None:
            return False
        else:
            self.current = self.current.next
            return True

    def __iter__(self):
        return LinkedListIterator(self.head)
