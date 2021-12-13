from linear_search import seq_search_for

print('실수를 검색합니다.')
print('End를 입력하면 입력을 종료합니다.')

num = 0
x = []

while True:
    s = input(f'x[{num}]: ')

    if s.upper() == 'END':
        break

    x.append(s)
    num += 1

key = input('검색할 값을 입력해주세요.')

idx = seq_search_for(x, key)

if idx == -1:
    print('검색 값을 갖는 원소가 존재하지 않습니다.')

else:
    print(f'검색 값은 {idx}에 있습니다.')
