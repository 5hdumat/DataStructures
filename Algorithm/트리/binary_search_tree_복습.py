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

            if p.key == key:
                return p.value
            elif p.key > key:
                p = p.left
            elif p.key < key:
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
            p = self.root

            while p is not None:
                if key == p.key:
                    return False
                elif key < p.key:
                    if p.left is None:
                        p.left = Node(key, value)
                        break
                    else:
                        p = p.left
                else:
                    if p.right is None:
                        p.right = Node(key, value)
                        break
                    else:
                        p = p.right

            return True

    def remove(self, key):
        p = self.root
        parent = None
        is_child_left = True

        while True:
            if p is None:
                return False

            if key == p.key:
                break
            else:
                parent = p
                if key < p.key:
                    p = p.left
                    is_child_left = True
                else:
                    p = p.right
                    is_child_left = False

        # 삭제 대상 노드의 자식 노드가 오른쪽에만 있을 때
        if p.left is None:
            if p is self.root:
                self.root = p.right
            elif is_child_left:
                parent.left = parent.right
            else:
                parent.left = parent.right
        elif p.right is None:
            if p is self.root:
                self.root = p.left
            elif is_child_left:
                parent.left = parent.left
            else:
                parent.left = parent.left
        else:
            parent = p
            child = p.left
            is_child_left = True

            while child.right is not None:
                parent = child
                child = child.right
                is_child_left = False

            p.key = child.key
            p.value = child.value

            if is_child_left:
                parent.left = child.left
            else:
                parent.right = child.left

        return True

    def dump(self):
        def _dumpp(node):
            if node is not None:
                _dumpp(node.left)
                print(f'{node.key}: {node.value}')
                _dumpp(node.right)

        _dumpp(self.root)
