'''
해시 충돌이 발생했을 때 해결하는 또 다른 방법은 오픈 주소법(open addressing)이다.
오픈 주소법은 충돌이 발생했을 때 재새히를 수행하여 빈 버킷을 찾는 방법을 말하며 닫힌 해시법이라고 한다.
빈 버킷이 나올 때까지 재해시하므로 선형 탐사법(linear probing) 이라고도 한다.
'''
from __future__ import annotations
from enum import Enum
from typing import Any
import hashlib


class Status(Enum):
    OCCUPIED = 0  # 데이터를 저장
    EMPTY = 1  # 비어있음
    DELETED = 2  # 삭제 완료


class Bucket:
    def __init__(self, key: Any = None, value: Any = None, stat: Status = Status.EMPTY) -> None:
        self.key = key
        self.value = value
        self.stat = stat

    def set_status(self, stat: Status) -> None:
        self.stat = stat


class OpenHash:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.table = [Bucket()] * self.capacity

    def hash_value(self, key: Any) -> None:
        if isinstance(key, int):
            return key % self.capacity

        return int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity

    # 재해시를 위한 식 (key + 1) % capacity (교재 p.145 참고)
    def rehash_value(self, key: Any) -> None:
        return (key + 1) % self.capacity

    def search_node(self, key: Any) -> Any:
        hash = self.hash_value(key)
        p = self.table[hash]

        for _ in range(self.capacity):
            if p.stat == Status.EMPTY:
                break
            elif p.stat == Status.OCCUPIED and p.key == key:
                return p

            rehash = self.rehash_value(hash)
            p = self.table[rehash]

        return None

    def search(self, key: Any) -> Any:
        p = self.search_node(key)

        if p is not None:  # 검색 성공
            return p.value
        else:
            return None  # 검색 실패

    def add(self, key: Any, value: Any) -> None:
        if self.search(key) is not None:
            return False  # 이미 동일한 키가 존재함

        hash = self.hash_value(key)
        p = self.table[hash]

        for _ in range(self.capacity):
            if p.stat == Status.EMPTY or p.stat == Status.DELETED:
                self.table[hash] = Bucket(key, value, Status.OCCUPIED)
                return True

            hash = self.rehash_value(hash)
            p = self.table[hash]

        return False # 해시테이블이 가득 참

    def remove(self, key: Any) -> int:
        p = self.search_node(key)

        if p is None:
            return False

        p.set_status(Status.DELETED)
        return True

    def dump(self) -> None:
        for i in range(self.capacity):
            stat = self.table[i].stat

            print(f'{i:2}', end=' ')
            if stat == Status.OCCUPIED:
                print(f'{self.table[i].key} ({self.table[i].value})')
            elif stat == Status.DELETED:
                print('--삭제 완료--')
            elif stat == Status.EMPTY:
                print('--비어 있음--')
