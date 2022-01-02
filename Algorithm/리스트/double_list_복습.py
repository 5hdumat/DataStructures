class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev or self
        self.next = next or self


class DoubleLinkedListIterator:
    def __init__(self, head):
        self.head = head
        self.current = head.next

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is self.head:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data


class DoubleLinkedListReverseIterator:
    def __init__(self, head):
        self.head = head
        self.current = head.prev

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is self.head:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.prev
            return data


class DoubleLinkedList:
    def __init__(self):
        self.current = self.head = Node()
        self.no = 0

    def __len__(self):
        return self.no

    def is_empty(self):
        return self.head.next is self.head

    def search(self, data):
        cnt = 0
        ptr = self.head

        while ptr.next is not self.head:
            if ptr.data == data:
                self.current = ptr
                return cnt

            cnt += 1
            ptr = self.head.next

        return -1

    def __contains__(self, data):
        return self.search(data) >= 0

    # 주목 노드 위치에 새로운 노드 삽입
    def add(self, data):
        node = Node(data, self.current, self.current.next)
        self.current.next.prev = node
        self.current.next = node
        self.current = node
        self.no += 1

    def add_first(self, data):
        self.current = self.head
        self.add(data)

    def add_last(self, data):
        self.current = self.head.prev
        self.add(data)

    def remove_current_node(self, data):
        if not self.is_empty():
            self.current.next.prev = self.current.prev
            self.current.prev.next = self.current.next
            self.current = self.current.prev
            self.no -= 1

            if self.current is self.head:
                self.current = self.current.next

    def remove_first(self):
        self.current = self.head
        self.remove_current_node()

    def remove_last(self):
        self.current = self.head.prev
        self.remove_current_node()

    def print_current_node(self):
        if self.is_empty():
            print('주목 노드가 존재하지 않습니다.')
        else:
            print(self.current.data)

    def print(self):
        ptr = self.head.next

        while ptr is not self.head:
            print(ptr.data)
            ptr = ptr.next

    def print_reverse(self):
        ptr = self.head.prev

        while ptr is not self.head:
            print(ptr.data)
            ptr = ptr.prev

    def next(self):
        if self.is_empty() or self.current.next is self.head:
            return False
        else:
            self.current = self.current.next
            return True

    def prev(self):
        if self.is_empty() or self.current.prev is self.head:
            return False
        else:
            self.current = self.current.prev
            return True

    def clear(self):
        ptr = self.head.next

        while not self.is_empty():
            self.remove_first()

        self.no = 0

    def __iter__(self):
        return DoubleLinkedListIterator(self.head)

    def __reversed__(self):
        return DoubleLinkedListReverseIterator(self.head)
