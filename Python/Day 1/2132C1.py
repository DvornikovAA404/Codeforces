t = int(input())
for _ in range(t):
    n = int(input())
    res = 0
    x = 0
    while n > 0:
        m = n%3
        n  = n//3
        res += m*(3 **(x+1) + x * (3 ** (x-1)))
        x += 1

    print(int(res))