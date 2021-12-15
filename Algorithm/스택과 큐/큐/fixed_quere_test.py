from fixed_queue_복습 import FixedQueue
from enum import Enum

Menu = Enum('Menu', ['인큐', '디큐', '피크', '검색', '덤프', '종료'])


def select_menu():
    s = [f'({m.value}) {m.name}' for m in Menu]
    print(*s, end='')
    n = int(input(': '))

    if 1 <= n <= len(Menu):
        return Menu(n)

q = FixedQueue(64) # 최대 64개를 인큐할 수 있는 큐 생성

while True:
    menu = select_menu()

    if menu == Menu.인큐:
        x = int(input('인큐할 데이터를 입력하세요:'))

        try:
            q.enqueue(x)
        except FixedQueue.FullError:
            print('큐가 가득 찼습니다.')

    elif menu == Menu.디큐:
        try:
            x = q.dequeue()
            print(f'디큐한 데이터는 [{x}] 입니다.')
        except FixedQueue.EmptyError:
            print('큐가 비어있습니다.')

    elif menu == Menu.피크:
        try:
            x = q.peek()
            print(f'피크한 데이터는 [{x}] 입니다.')
        except FixedQueue.EmptyError:
            print('큐가 비어있습니다.')

    elif menu == Menu.검색:
        x = int(input('검색할 데이터를 입력해주세요: '))

        if x in q:
            print(f'검색한 데이터의 맨 앞 위치는 [{q.find(x)}]이며, 큐에 [{q.count(x)}]개 존재합니다.')
        else:
            print('검색할 데이터가 큐에 존재하지 않습니다.')

    elif menu == Menu.덤프:
        q.dump()

    elif menu == Menu.종료:
        break
