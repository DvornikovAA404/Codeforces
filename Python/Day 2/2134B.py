def get_primes(x):
    s = set()
    d = 2
    tmp = x
    while d * d <= tmp:
        if tmp % d == 0:
            s.add(d)
            while tmp % d == 0:
                tmp //= d
        d += 1
    if tmp > 1:
        s.add(tmp)
    return s

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    first = a[0]
    cand = get_primes(first) | get_primes(first + k)
    cand = sorted(list(cand))
    
    ans = ""
    
    for d in cand:
        curr_res = []
        ok = True
        
        if k % d == 0:
            for x in a:
                if x % d != 0:
                    ok = False
                    break
                curr_res.append(str(x))
        else:
            inv = pow(k, d - 2, d)
            for x in a:
                rem = x % d
                if rem == 0:
                    curr_res.append(str(x))
                else:
                    ops = ((d - rem) * inv) % d
                    if ops > k:
                        ok = False
                        break
                    curr_res.append(str(x + ops * k))
        
        if ok:
            ans = " ".join(curr_res)
            break
            
    print(ans)