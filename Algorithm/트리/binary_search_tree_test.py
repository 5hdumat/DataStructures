from binary_search_tree_복습 import BinarySearchTree
from enum import Enum

Menu = Enum('Menu', ['삽입', '삭제', '검색', '덤프', '키의범위', '종료'])


def select_menu():
    s = [f'({m.value}) {m.name}' for m in Menu]
    while True:
        print(*s, sep=' ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)


tree = BinarySearchTree()

while True:
    menu = select_menu()

    if menu == Menu.삽입:
        key = int(input('삽입할 키를 입력하세요: '))
        value = input('삽입할 값을 입력하세요: ')
        if not tree.add(key, value):
            print('삽입에 실패했습니다.')

    elif menu == Menu.삭제:
        key = int(input('삭제할 키를 입력하세요: '))
        tree.remove(key)

    elif menu == Menu.검색:
        key = int(input('검색할 키를 입력하세요.:'))
        search = tree.search(key)

        if search is not None:
            print(f'{search}')
        else:
            print('해당하는 데이터가 없습니다.')

    elif menu == Menu.덤프:
        tree.dump()

    elif menu == Menu.키의범위:
        print(f'키의 최솟값은 {tree.min_key()}')
        print(f'키의 최댓값은 {tree.max_key()}')

    else:
        break
