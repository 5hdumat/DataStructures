counter = 0
ptr = 0
prime = [None] * 500

prime[ptr] = 2
ptr += 1

# 4 이상의 짝수는 어차피 2로 나누어 떨어지므로 간단히 패스
for n in range(3, 1001, 2):
    for i in range(1, ptr): # range범위가 같으면 바로 else로 탄다. (ex. for i in range(1,1)) 원소를 지금까지 구한 소수로만 나눗셈한다.
        counter += 1

        if n % prime[i] == 0:
            break
    else:
        prime[ptr] = n
        ptr += 1

for i in range(ptr):
    print(prime[i])

print(f'총 나눗셈을 실행한 횟수: {counter}')


# 소스는 n의 제곱근 이하의 어떤 소수로도 나누어 떨어지지 않는다.는 점을 이용한 풀이개선
counter = 0
ptr = 0
prime = [None] * 500 # 짝수는 소수가 아니므로 전체 개수 1000의 반으로 모든 소수를 배열에 넣을 수 있기 때문에 500으로 지정한다.

prime[ptr] = 2
ptr += 1

prime[ptr] = 3
ptr += 1

# 소수만 판단 (짝수는 그냥 소수가 아니라고 외우자)
for n in range(5, 1001, 2):
    i = 1

    # n의 제곱근을 구하는 것보다 소수들을 제곱하는게 더 간편
    # 7의 제곱근 2.64575131106 보다 작은 소수 2와 비교하나 (2 <= 2.64575131106)
    # 7과 2의 제곱은 4 (4 <= 7) 를 비교하나 동일하다.
    while prime[i] * prime[i] <= n:
        counter += 2
        if prime[i] % n == 0:
            break
        i += 1
    else:
        prime[ptr] = n
        ptr += 1
        counter += 1

print(f'총 곱셈과 나눗셈을 한 횟수는 {counter}')
