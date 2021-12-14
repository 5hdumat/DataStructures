from open_hash_복습 import OpenHash
from enum import Enum

Menu = Enum('Menu', ['추가', '삭제', '검색', '덤프', '종료'])


def select_menu() -> Menu:
    s = [f'({m.value}) {m.name}' for m in Menu]
    print(*s, end=' ')

    n = int(input(': '))
    if 1 <= n <= 4:
        return Menu(n)


hash = OpenHash(13)

while True:
    menu = select_menu()

    if menu == Menu.추가:
        key = int(input('추가할 키를 입력해주세요.: '))
        value = input('추가할 값을 입력해주세요.: ')

        if not hash.add(key, value):
            print('값을 추가하지 못했습니다.')

    elif menu == Menu.삭제:
        key = int(input('삭제할 키를 입력해주세요.: '))

        if not hash.remove(key):
            print('값을 삭제하지 못했습니다.')

    elif menu == Menu.검색:
        key = int(input('검색할 키를 입력해주세요.: '))
        search = hash.search(key)

        if not search:
            print('키값을 찾지 못했습니다.')
        else:
            print(f'검색한 키의 값을 {search}입니다.')

    elif menu == Menu.덤프:
        hash.dump()

    elif menu == Menu.종료:
        break