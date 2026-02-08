t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    sum_free = 0
    max_c = 0
    for _ in range(n):
        a, b, c = map(int, input().split())
        
        free = a * (b - 1)
        sum_free += free
        cycle = a * b - c
        if cycle > max_c:
            max_c = cycle

            
    if sum_free >= x:
        print(0)
        continue
    rem = x - sum_free
    if max_c == 0:
        print(-1)
        continue
    print((rem+max_c-1)//max_c)