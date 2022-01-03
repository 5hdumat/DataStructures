'''
이진 검색 트리

이진 검색 트리는 모든 노드가 다음 조건을 만족해야 한다.
- 왼쪽 서브 트리에 있는 노드 키 값이 자신의 노드 키 값보다 작아야 한다.
- 오른쪽 서브 트리에 있는 노드 키 값이 자신의 노드 키 값보다 커야한다.

이러한 조건 때문에 이진 검색 트리는 중위 순회만으로 오름차순된 노드 목록을 얻을 수 있다.
'''


class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left  # 왼쪽 노드
        self.right = right  # 오른쪽 노드


class BinarySearchTree:
    def __init__(self):
        self.root = None  # 루트 노드

    '''
    키 값으로 노드를 검색하는 함수
    
    이진 검색 트리의 특징을 이용해 찾고자하는 노드보다 비교 대상 노드가 작으면 왼쪽 노드를 크면 오른쪽 노드를 탐색한다.
    (위 작업을 반복하며, 레벨을 하나씩 늘려간다.)
    '''

    def search(self, key):
        p = self.root

        while True:
            if p is None:
                return None

            if p.key == key:
                return p
            elif p.key < key:
                p = p.left
            else:
                p = p.right

    def add(self, key, value):
        def add_node(node, key, value):
            if node.key == key:
                return False
            elif node.key > key:
                if node.left is None:
                    node.left = Node(key, value)
                else:
                    add_node(node.left, key, value)
            else:
                if node.right is None:
                    node.right = Node(key, value)
                else:
                    add_node(node.right, key, value)

            return True

        if self.root is None:
            self.root = Node(key, value)
            return True

        else:
            return add_node(self.root, key, value)

    def remove(self, key):
        p = self.root
        parent = None  # 부모 노드
        is_left_child = True  # 삭제 대상 노드가 부모 노드의 왼쪽 자식인지 아닌지 판단

        while True:
            if p is None:
                return False

            if key == p.key:  # 삭제 대상 노드를 찾았으면 break
                break
            else:
                parent = p  # 부모 노드 미리 설정
                if key < p.key:
                    p = p.left
                    is_left_child = True
                else:
                    p = p.right
                    is_left_child = False

        # 삭제 노드의 왼쪽 자식 노드가 없다면
        if p.left is None:
            if p is self.root:
                self.root = p.right
            elif is_left_child:
                parent.left = p.right
            else:
                parent.right = p.right
        elif p.right is None:
            if p is self.root:
                self.root = p.left
            elif is_left_child:
                parent.left = p.left
            else:
                parent.right = p.left
        else:
            parent = p
            child = p.left
            is_left_child = True

            while child.right is not None:
                parent = child
                child = child.right
                is_left_child = False

            p.key = child.key
            p.value = child.value

            # 자식이 오른쪽 노드를 가지고 있지 않으면
            if is_left_child:
                parent.left = child.left  # 부모 노드의 왼쪽 노드를 자식의 left 노드로 하거나 삭제
            else:
                parent.right = child.left  # 부모 노드의 오른쪽 노드를 자식의 left로 하거나 삭제

    def dump(self, reverse=False):
        def _print_subtree(node):
            if node is not None:
                _print_subtree(node.left)
                print(f'{node.key}: {node.value}')
                _print_subtree(node.right)

        def _print_subtree_rev(node):
            if node is not None:
                _print_subtree_rev(node.right)
                print(f'{node.key}: {node.value}')
                _print_subtree_rev(node.left)

        if not reverse:
            _print_subtree(self.root)
        else:
            _print_subtree_rev(self.root)

    def min_key(self):
        if self.root is None:
            return None

        p = self.root
        while p.left is not None:
            p = p.left

        return p.key

    def max_key(self):
        if self.root is None:
            return None

        p = self.root
        while p.right is not None:
            p = p.right

        return p.key
