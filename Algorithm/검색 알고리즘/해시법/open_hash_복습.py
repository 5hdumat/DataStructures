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
    OCCUPIED = 0  # 테이블에 저장
    EMPTY = 1  # 비어 있음
    DELETED = 2  # 삭제 완료


class Bucket:
    def __init__(self, key=None, value=None, stat=Status.EMPTY):
        self.key = key
        self.value = value
        self.stat = stat

    def set(self, stat):
        self.stat = stat


class OpenHash:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [Bucket()] * self.capacity

    def hash_value(self, key):
        if isinstance(key, int):
            return key % self.capacity

        return int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity

    def rehash_value(self, key):
        return (key + 1) % self.capacity

    def search_node(self, key):
        hash = self.hash_value(key)
        p = self.table[hash]

        for _ in range(self.capacity):
            if p.stat == Status.EMPTY:
                break  # 해시테이블이 비어있으면 None 출력
            elif p.stat == Status.OCCUPIED and p.key == key:  # 노드가 생성된 상태인데 키가 동일하면 반환
                return p

            hash = self.rehash_value(hash)
            p = self.table[hash]

        return None

    def search(self, key) -> bool:
        p = self.search_node(key)

        if p is not None:
            return p.value
        else:
            return None

    def add(self, key, value) -> bool:
        if self.search(key) is not None:
            return False  # 동일한 키가 이미 존재함

        hash = self.hash_value(key)
        p = self.table[hash]

        for _ in range(self.capacity):
            if p.stat in (Status.EMPTY, Status.DELETED):
                self.table[hash] = Bucket(key, value, Status.OCCUPIED)
                return True

            hash = self.rehash_value(hash)  # 인자로 왜 자꾸 key를 넘기지 ... hash로 넘겨야함 (변수명도 상단 멤버변수가 변경되도록 일치시켜야함)
            p = self.table[hash]

        return False  # 해시테이블 가득 참

    def remove(self, key):
        p = self.search_node(key)

        if p is None:
            return False

        p.set(Status.DELETED)
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
