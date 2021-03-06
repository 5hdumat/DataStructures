'''
앝은 복사 (copy, 원소 수준의 복사)

얕은 복사에서는 리스트 안의 모든 원소가 참조하는 곳까지 복사된다.
그러므로 리스트 x의 참조 객체 id가 달라지면 y의 참조 객체 id도 달라진다.

얕은 복사는 참조 값(식별번호)만을 복사한다.
'''
import copy

x = [[1, 2, 3], [4, 5, 6]]

# copy()를 사용한 뒤
y = x.copy()

# x[0][1] 값을 9로 업데이트하면 y의 원소도 변경된다.
x[0][1] = 9
print(x, y, sep='\n') # [[1, 9, 3], [4, 5, 6]] [[1, 9, 3], [4, 5, 6]]

'''
깊은 복사 (deepcopy, 구성 원소 수준의 복사)

얕은 복사는 참조 값까지 복사하므로 원본 데이터의 값이 달라지면 카피 데이터의 값까지 달라진다.
이러한 상황을 피하려면 구성 원소 수준의 복사가 필요하며, 이를 깊은 복사라고 한다.

깊은 복사는 참조 값(식별번호) 뿐만 아니라 참조하는 객체 자체를 '전체 복사'한다.
'''

x = [[1, 2, 3], [4, 5, 6]]

y = copy.deepcopy(x) # x를 y로 깊은 복사
x[0][1] = 9

print(x, y, sep='\n') # 배열 y는 x의 영향을 받지 않음


