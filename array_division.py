def can_divide(arr, n, k, max_sum):
    # Ez a függvény eldönti, hogy lehetséges-e k darab rész-tömböt létrehozni úgy,
    # hogy egyik rész-tömb összeg sem haladja meg max_sum értékét.
    current_sum = 0
    subarrays = 1  # Az első rész-tömb már kezdődik

    for num in arr:
        if current_sum + num > max_sum:
            subarrays += 1  # Új rész-tömb kezdődik
            current_sum = num  # Az új rész-tömb kezdődik az aktuális elemmel
            if subarrays > k:
                return False  # Túl sok rész-tömb lenne
        else:
            current_sum += num  # Hozzáadjuk a számot az aktuális rész-tömbhöz

    return True

def minimize_max_subarray_sum(n, k, arr):
    # Bináris keresés a legnagyobb rész-tömb összegére
    left, right = max(arr), sum(arr)
    
    while left < right:
        mid = (left + right) // 2
        if can_divide(arr, n, k, mid):
            right = mid  # Ha lehetséges, próbálkozunk egy kisebb maximális összeggel
        else:
            left = mid + 1  # Ha nem lehetséges, akkor növelnünk kell a maximális összeget

    return left

# Bemenet
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Eredmény
print(minimize_max_subarray_sum(n, k, arr))
