def main():
    mod = 20180113
    [n, m, k, l] = [int(i) for i in input().split()]
    x = int(input())
    all = [0] * x
    nw = [0] * x
    nw[0] = l
    all[0] = l 
    for i in range(1, x):
        nw[i] = 0 if i == 1 else nw[i - 1]
        if i >= m:
            nw[i] += nw[i - m]
        if i >= m + k:
            nw[i] -= nw[i - m - k]
        nw[i] = (nw[i] + mod) % mod
        all[i] = all[i - 1]
        if (i >= n):
            all[i] -= nw[i-n]
        all[i] += nw[i]
        all[i] = (all[i] + mod) % mod
    print(all[x-1])

if __name__ == "__main__":
    main()