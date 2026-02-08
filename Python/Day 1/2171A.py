t = int(input())
for _ in range(t):
    n = int(input())
    if n%2!=0:
        print(0)
    else:
        m = n//2
        print(m//2+1)