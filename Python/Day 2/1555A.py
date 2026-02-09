t = int(input())
for _ in range(t):
    n = max(int(input()), 6)
    pcs = n + (n%2)
    time = (5 * pcs)//2
    print(int(time))