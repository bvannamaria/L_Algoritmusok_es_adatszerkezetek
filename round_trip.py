import sys
sys.setrecursionlimit(200000)

def find_kor(n, adj):
    latogat = [False] * (n + 1)
    os = [-1] * (n + 1) #ős/ származtatott/ szülő
    ut = []

    def dfs(v):
        latogat[v] = True
        ut.append(v)
        
        for szomszed in adj[v]:
            if not latogat[szomszed]:
                os[szomszed] = v
                if dfs(szomszed):
                    return True
            elif szomszed != os[v]:  # Ha találtunk egy visszafelé irányuló élt (ciklus)
                # A ciklus visszaépítése
                kor = []
                kor.append(szomszed)
                idx = len(ut) - 1
                while ut[idx] != szomszed:
                    kor.append(ut[idx])
                    idx -= 1
                kor.append(szomszed)
                kor.reverse()
                print(len(kor))
                print(" ".join(map(str, kor)))
                return True
        
        ut.pop()
        return False

    for i in range(1, n + 1):
        if not latogat[i]:
            if dfs(i):
                return
    
    print("IMPOSSIBLE")

# Bemenelet olvasása
n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]

# Útvonalak beolvasása és a szomszédsági lista létrehozása
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

# Ciklus keresése és kiírása, ha létezik
find_kor(n, adj)
