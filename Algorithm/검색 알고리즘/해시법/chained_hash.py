'''
해시값이 충돌하는 경우 체인법과 오픈 주소법으로 해결할 수 있는데 해당 모듈은 체인법이다.

해시값과 키는 일반적으로 1:n구조이다.
'''

from __future__ import annotations
from typing import Any, Type
import hashlib


# 노드 클래스는 키와 값이 짝을 이루는 구조이다.
class Node:
    def __init__(self, key: Any, value: Any, next: Node) -> None:
        self.key = key
        self.value = value
        self.next = next # 뒤쪽 노드를 참조, table[4] -> 69 -> 17 이라면 table[4]는 버킷 69 참조 -> 버킷 69는 버킷 17참조 -> 버킷 17은 더 이상 노드가 존재하지 않음을 알려주는 None 을 참조한다.


class ChainedHash:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.table = [None] * self.capacity

    def hash_value(self, key: Any):
        # 찾고자 하는 key가 int라면
        if isinstance(key, int):
            return key % self.capacity

        # 실수라면
        return int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity

    def search(self, key: Any) -> Any:
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return p.value

            p = p.next

        return None

    def add(self, key: Any, value: Any) -> bool:
        hash = self.hash_value(key)
        p = self.table[hash]

        # 연결 리스트가 비어있지 않다면
        while p is not None:
            if p.key == key:  # 추가할 키가 이미 존재한다면 실패처리 (노드는 key, value 구조로 추가, 여기에서의 key가 중복되면 안됨)
                return False

            p = p.next

        tmp = Node(key, value, self.table[hash])
        self.table[hash] = tmp

        return True

    def remove(self, key: Any) -> bool:
        hash = self.hash_value(key)
        p = self.table[hash]
        pp = None

        # 파이썬은 객체 참조 방식이기 때문에
        # 해시 테이블의 버킷이 바라보는 참조 값이 삭제해야할 노드라면 그 다음 노드를 참조하게 한거나
        # 노드가 바라보는 다음 노드가 삭제해야할 노드라면 삭제해야할 노드 다음 노드를 참조하게 한다.
        # 그게 곧 파이썬에선 삭제이다.
        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next

                return True

            pp = p
            p = p.next

        return False

    # 모든 원소를 출력
    def dump(self) -> None:
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')

            while p is not None:
                print(f' -> {p.key} ({p.value})', end='')
                p = p.next

            print()
