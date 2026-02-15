t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    i = 1
    while i < n:
        if a[i] == a[i-1] or a[i] == 7-a[i-1]:
            sum += 1
            i += 1
        i += 1
    print(sum)