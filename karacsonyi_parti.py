MOD = 10**9 + 7

def derangements(n):
    # Ha csak 1 gyerek van, nincs érvényes permutáció (mert mindenkinek saját ajándékot adna)
    if n == 1:
        return 0
    # Ha két gyerek van, akkor egyféleképpen lehet szétosztani
    if n == 2:
        return 1
    
    # Létrehozzuk a DP tömböt, hogy kiszámoljuk a derangementeket
    dp = [0] * (n + 1)
    
    # Alapértékek
    dp[1] = 0
    dp[2] = 1
    
    # Kitöltjük a DP tömböt a képlettel
    for i in range(3, n + 1):
        dp[i] = (i - 1) * (dp[i - 1] + dp[i - 2]) % MOD
    
    return dp[n]

# Bemenet beolvasása
n = int(input())

# Eredmény kiírása
print(derangements(n))
