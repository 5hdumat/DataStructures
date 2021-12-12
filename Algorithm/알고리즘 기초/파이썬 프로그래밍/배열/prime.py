counter = 0
ptr = 0
prime = [None] * 500

prime[ptr] = 2
ptr += 1

# 4 이상의 짝수는 어차피 2로 나누어 떨어지므로 간단히 패스
for n in range(3, 1001, 2):
    for i in range(1, ptr): # range범위가 같으면 바로 else로 탄다. 원소를 지금까지 구한 소수로만 나눗셈한다.
        counter += 1

        if n % prime[i] == 0:
            break
    else:
        prime[ptr] = n
        ptr += 1

for i in range(ptr):
    print(prime[i])

print(f'총 나눗셈을 실행한 횟수: {counter}')