def calculate_details(n, k, m):
    units_per_k = k // m
    if units_per_k == 0:
        return 0
    units_per_k_weight = units_per_k * m
    details_count = 0
    while n >= k:
        workpieces = n // k
        n -= workpieces * units_per_k_weight
        details_count += workpieces * units_per_k
    return details_count


n, k, m = map(int, input().split())
print(calculate_details(n, k, m))
