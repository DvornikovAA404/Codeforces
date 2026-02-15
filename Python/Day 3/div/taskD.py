t = int(input())
for _ in range(t):
    n = int(input())
    f = list(map(int, input().split()))
    a = []
    S = (f[0]+f[n-1])//(n-1)
    a1 = (f[1]-f[0]+S)//2
    an = (S-(f[n-1]-f[n-2]))//2
    a.append(a1)
    for i in range(1, n-1):
        ai = f[i-1] + f[i+1] - 2*f[i]
        a.append(ai//2)
    a.append(an)
    print(*a)