def get_divisors(n):
    divs = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divs.append(i)
            if i*i != n:
                divs.append(n // i)
    return sorted(divs)

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    mask = [0] * n
    for i in range(k):
        arr = input()
        for j in range(n):
            bit = ord(arr[j]) - ord('a')
            mask[j] |= (1<<bit)
    ds = get_divisors(n)
    m = 1
    s = ""
    for d in ds:
        s = ""
        m = n//d
        fail = False
        for i in range(d):
            res = mask[i]
            for l in range(i+d, n, d):
                res = res & mask[l]
                if res == 0:
                    fail = True
                    break
            if fail:
                break
            s += chr(ord('a') + res.bit_length() - 1)
        if not fail:
            print(s*m)
            break