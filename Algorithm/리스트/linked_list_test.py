from enum import Enum
from linked_list_복습 import LinkedList

Menu = Enum('Menu', ['머리에노드삽입', '꼬리에노드삽입', '머리노드삭제',
                     '꼬리노드삭제', '주목노드출력', '주목노드한칸뒤로이동',
                     '주목노드삭제', '모든노드삭제', '검색', '멤버십판단',
                     '모든노드출력', '스캔', '종료'])


def select_menu():
    s = [f'({m.value}) {m.name}' for m in Menu]

    while True:
        print(*s, sep=' ', end='')
        n = int(input(': '))

        if 1 <= n <= len(Menu):
            return Menu(n)


lst = LinkedList()

while True:
    menu = select_menu()

    if menu == Menu.머리에노드삽입:
        lst.add_first(int(input('머리 노드에 넣을 값을 입력하세요: ')))

    elif menu == Menu.꼬리에노드삽입:
        lst.add_last(int(input('머리 노드에 넣을 값을 입력하세요: ')))

    elif menu == Menu.머리노드삭제:
        lst.remove_first()

    elif menu == Menu.꼬리노드삭제:
        lst.remove_last()

    elif menu == Menu.주목노드출력:
        lst.print_current_node()

    elif menu == Menu.주목노드한칸뒤로이동:
        lst.next()

    elif menu == Menu.주목노드삭제:
        lst.remove_current_node()

    elif menu == Menu.모든노드삭제:
        lst.clear()

    elif menu == Menu.검색:
        search = lst.search(int(input('검색할 값을 입력하세요: ')))

        if search >= 0:
            print(f'그 값의 데이터는 {search + 1}번째에 있습니다.')
        else:
            print('해당하는 데이터가 없습니다.')

    elif menu == Menu.멤버십판단:
        search = int(input('판단할 값을 입력하세요: '))

        if search in lst:
            print('그 값의 데이터는 포함되어 있습니다.')
        else:
            print('그 값의 데이터는 포함되어 있지 않습니다.')

    elif menu == Menu.모든노드출력:
        lst.print()

    elif menu == Menu.스캔:
        for e in lst:
            print(e)

    else:
        break
