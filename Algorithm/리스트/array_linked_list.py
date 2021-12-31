'''
[커서를 이용한 연결 리스트]
데이터의 개수가 크게 변하지 않거나 데이터의 최대 개수를 예측할 수 있는 경우라면 커서를 이용한 연결 리스트를 사용하여 효율적 운용이 가능하다.
포인터는 따로 크기를 지정하지 않기 때문에 노드를 추가, 삭제할때마다 메모리를 확보하고 해제하는 비용이 든다.
커서는 배열을 사용하여 삭제된 레코드를 기억해두고 메모리 공간을 재활용한다.

근본적으로는 포인터를 이용한 연결 리스트와 거의 대응한다.
단지 커서를 이용하면 노드의 삽입과 삭제에 따른 원소의 이동이 '처음부터' 불필요하다는 점에서 포인터 연결리스트와 차이점을 가진다.
'''
from __future__ import annotations

Null = -1


class Node:
    def __init__(self, data=Null, next=Null, dnext=Null):
        self.data = data  # 데이터
        self.next = next  # 리스트의 뒤쪽 포인터
        self.dnext = dnext  # 프리 리스트의 뒤쪽 포인터


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
        self.head = Null  # 머리 노드 인덱스
        self.current = Null  # 주목 노드 인덱스
        self.max = Null  # 사용 중인 꼬리 노드 인덱스
        self.deleted = Null  # 프리 리스트의 머리 노드
        self.capacity = capacity  # 리스트의 크기
        self.n = [Node()] * self.capacity  # 리스트 본체
        self.no = 0

    def __len__(self):
        return self.no

    # 다음에 삽입할 레코드의 인덱스 구하기
    def get_insert_index(self) -> int:
        # 삭제 레코드가 존재하지 않으면
        if self.deleted == Null:
            if self.max + 1 < self.capacity:
                self.max += 1
                return self.max  # 새 레코드 사용
            else:
                return -1  # 크기 초과
        else:
            rec = self.deleted
            self.deleted = self.n[rec].dnext  # 프리 리스트에서 맨 앞 rec 꺼내기
            return rec

    # 레코드 인덱스를 프리 리스트에 등록
    def delete_index(self, idx):
        # 삭제 레코드가 존재하지 않으면
        if self.deleted == Null:
            self.deleted = idx
            self.n[idx].dnext = Null  # idx를 프리 리스트의 맨 앞에 등록
        else:
            rec = self.deleted
            self.deleted = idx
            self.n[idx].dnext = rec

    # data와 값이 같은 노드 검색
    def search(self, data) -> int:
        cnt = 0
        ptr = self.head  # 헤드 노드에서부터 순차검색
        while ptr != Null:
            if self.n[ptr].data == data:
                self.current = ptr
                return cnt

            cnt += 1
            ptr = self.n[ptr].next  # 뒤쪽 노드에 주목

        return -1

    def __contains__(self, data):
        return self.search(data) >= 0

    def add_first(self, data):
        ptr = self.head
        rec = self.get_insert_index()

        if rec != Null:
            self.head = self.current = rec
            self.n[self.head] = Node(data, ptr)
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
            self.delete_index(self.head)
            self.head = self.current = ptr
            self.no -= 1

    def remove_last(self):
        if self.head != Null:
            # 노드가 1개뿐이라면 머리노드 삭제 함수 호출
            if self.n[self.head].next == Null:
                self.remove_first()
            else:
                ptr = self.head
                pre = self.head

                while self.n[ptr].next != Null:
                    pre = ptr
                    ptr = self.n[ptr].next

                self.n[pre].next = Null
                self.delete_index(ptr)
                self.current = pre
                self.no -= 1

    # 특정 레코드 삭제
    def remove(self, p):
        if self.head != Null:
            if p == self.head:
                self.remove_first()
            else:
                ptr = self.head

                while self.n[ptr].next != p:
                    ptr = self.n[ptr].next
                    if ptr == Null:
                        return

                self.delete_index(p)
                self.n[ptr].next = self.n[p].next
                self.current = ptr
                self.no -= 1

    # 주목 노드 삭제
    def remove_current_node(self):
        self.remove(self.current)

    def clear(self):
        while self.head != None:
            self.remove_first()
        self.current = Null

    def next(self) -> bool:
        if self.current == Null or self.n[self.current].next == Null:
            return False

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

        while self.n[ptr].next != Null:
            print(self.n[ptr].data)
            ptr = self.n[ptr].next

    def dump(self):
        for i in self.n:
            print(f'[{i}] {i.data} {i.next} {i.dnext}')

    def __iter__(self):
        return ArrayLinkedListIterator(self.n, self.head)
