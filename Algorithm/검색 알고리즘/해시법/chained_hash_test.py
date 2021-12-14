from enum import Enum

from chained_hash_복습 import ChainedHash

Menu = Enum('Menu', ['추가', '삭제', '검색', '덤프', '종료'])  # 메뉴 선언


def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]

    while True:
        print(*s, end=' ')
        n = int(input(': '))

        if 1 <= n <= len(Menu):
            return Menu(n)


hash = ChainedHash(13)  # 크기가 13인 해시 테이블을 생성한다.

while True:
    menu = select_menu()

    if menu == Menu.추가:
        key = int(input('추가할 키를 입력하세요.: '))
        val = input('추가할 값을 입력하세요.: ')

        if not hash.add(key, val):
            print('노드를 추가하지 못했습니다.')

    elif menu == Menu.삭제:
        key = int(input('삭제할 키를 입력하세요.: '))

        if not hash.remove(key):
            print('노드를 삭제하지 못했습니다.')

    elif menu == Menu.검색:
        key = int(input('검색할 키를 입력하세요: '))

        search = hash.search(key)

        if search is None:
            print('검색결과가 존재하지 않습니다.')
        else:
            print(f'검색한 키를 갖는 값은 {search} 입니다.')

    elif menu == Menu.덤프:
        hash.dump()

    elif menu == Menu.종료:
        break
