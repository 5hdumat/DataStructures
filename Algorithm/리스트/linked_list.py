from __future__ import annotations

from typing import Any


class Node:
    def __init__(self, data: Any = None, next: Node = None):
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
        self.no = 0  # 연결 리스트에 등록되어 있는 노드의 개수
        self.head = None  # 머리 노드에 대한 참조
        self.current = None  # 현재 주목하고 있는 노드에 대한 참조 (리스트에서 노드를 검색하여 그 노드를 주목한 직후에 노드를 삭제하는 등의 용도로 사용)

    def __len__(self):
        return self.no

    # 데이터 검색
    def search(self, data):
        cnt = 0
        ptr = self.head

        while ptr is not None:
            if ptr.data == data:
                self.current = ptr  # 찾은 노드 주목
                return cnt

            cnt += 1
            ptr = ptr.next  # 다음 노드 참조

        return -1

    # in 절 사용 가능
    def __contains__(self, data) -> bool:
        return self.search(data) >= 0

    # 리스트의 맨 앞(머리)에 노드 삽입
    def add_first(self, data):
        ptr = self.head  # 삽입하기 전의 머리 노드를 ptr에 참조해둔다.
        self.head = self.current = Node(data, ptr)
        self.no += 1

    # 리스트의 맨 뒤(꼬리)에 노드 삽입
    def add_last(self, data):
        # 리스트가 비어 있으면 맨 앞에 노드를 삽입
        if self.head is None:
            self.add_first(data)
        else:
            ptr = self.head

            while ptr.next is not None:
                ptr = ptr.next

            ptr.next = self.current = Node(data, None)
            self.no += 1

    # 머리 노드 삭제
    def remove_first(self):
        if self.head is not None:
            self.head = self.current = self.head.next

        self.no -= 1

    # 꼬리 노드 삭제
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

    # 임의의 노드를 삭제
    def remove(self, p):
        if self.head is not None:
            if p is self.head:
                self.remove_first()
            else:
                ptr = self.head

                # ptr.next == p 라면 반복문 종료
                while ptr.next is not p:
                    ptr = ptr.next

                    if ptr is None:
                        return

                # ptr이 참조하는 노드를 p가 참조하는 노드로 변경
                ptr.next = p.next
                self.current = ptr
                self.no -= 1

    # 가장 최근에 주목된 노드 삭제
    def remove_current_node(self):
        self.remove(self.current)

    # 전체 노드 삭제
    def clear(self):
        # 전체가 비어 있을 떄까지 머리노드부터 반보갛여 하나씩 삭제
        while self.head is not None:
            self.remove_first()
        self.current = None
        self.no = 0

    # 주목 노드를 한칸 뒤로 이동
    def next(self) -> bool:
        # 주목 노드가 없거나 주목 노드가 꼬리 노드일 경우 뒤로 이동할 수 없다.
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
