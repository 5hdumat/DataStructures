from enum import Enum

from fixed_stack_복습 import FixedStack

Menu = Enum('Menu', ['푸시', '팝', '피크', '검색', '덤프', '종료'])


def select_menu():
    s = [f'({m.value}) {m.name}' for m in Menu]
    print(*s, end='')
    n = int(input(': '))

    if 1 <= n <= len(Menu):
        return Menu(n)


s = FixedStack(64)  # 최대 64개를 푸시할 수 있는 스택 선언

while True:
    print(f'혀내 데이터 개수: {len(s)} / {s.capacity}')
    menu = select_menu()

    if menu == Menu.푸시:
        x = int(input('푸시하고자 하는 데이터를 입력하세요: '))

        try:
            s.push(x)
        except FixedStack.FullError:
            print('스택이 가득 차있습니다.')

    elif menu == Menu.팝:
        try:
            x = s.pop()
            print(f'팝한 데이터는 [{x}] 입니다.')
        except FixedStack.EmptyError:
            print('스택이 비어있습니다.')

    elif menu == Menu.피크:
        try:
            peek = s.peek()
            print(f'스택의 최상단에 있는 데이터는 [{peek}] 입니다.')
        except FixedStack.EmptyError:
            print('스택이 비어있습니다.')

    elif menu == Menu.검색:
        x = int(input('검색 하고자 하는 데이터를 입력하세요.'))

        if x in s:
            print(f'검색 하고자 하는 데이터의 위치 [{s.find(x)}] 이며, 스택에 [{s.count(x)}] 개 포함되어 있습니다.')
        else:
            print('검색 하고자 하는 데이터가 존재하지 않습니다.')

    elif menu == Menu.덤프:
        s.dump()

    elif menu == Menu.종료:
        break
