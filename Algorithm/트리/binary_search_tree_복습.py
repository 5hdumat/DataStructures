class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, key):
        p = self.root

        while True:
            if p is None:
                return None
            else:
                if key == p.key:
                    return p.value
                elif key < p.key:
                    p = p.left
                else:
                    p = p.right

    def add(self, key, value):
        def add_node(node, key, value):
            if key == node.key:
                return False

            elif key < node.key:
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
        parent = None
        is_left_child = True

        # 루트 노드부터 탐색하여 삭제 대상 노드 찾기
        while True:
            if p is None:
                return

            if key == p.key:
                break
            else:
                parent = p

                if key < p.key:
                    p = p.left
                    is_left_child = True
                else:
                    p = p.right
                    is_left_child = False

        # 왼쪽 노드가 없으면
        if p.left is None:
            if p is self.root:
                self.root = p.right
            elif is_left_child:
                parent.left = p.right
            else:
                parent.right = p.right

        # 오른쪽 노드가 없으면
        elif p.right is None:
            if p is self.root:
                self.root = p.left
            elif is_left_child:
                parent.left = p.left
            else:
                parent.right = p.left

        # 자식 노드가 2개 있으면
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

            if is_left_child:
                parent.left = child.left
            else:
                parent.right = child.left
