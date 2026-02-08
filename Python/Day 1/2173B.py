t = int(input())
for _ in range(t):
    n = int(input())
    a = input().split()
    b = input().split()
    k = 0
    new = [k, k]
    for i in range(n):
        v1 = new[1] - int(a[i])
        v12 = new[0] - int(a[i])
        v22 = int(b[i]) - new[1]
        v2 = int(b[i]) - new[0]
        new = [min(v1, v12, v22, v2), max(v1, v12, v22, v2)]
    print(max(new))