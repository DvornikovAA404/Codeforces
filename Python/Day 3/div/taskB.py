t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(1, n+1):
        sqi = i
        while sqi%2 == 0:
            sqi //= 2
        sqa = arr[i-1]
        while sqa%2 == 0:
            sqa //= 2
        if sqi != sqa:
            print("NO")
            break
    else:
        print("YES")