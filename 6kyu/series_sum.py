def series_sum(n):
    if n == 0:
        return "0.00"
    
    total = 0
    for i in range(1, n + 1):
        denominator = 3 * i - 2
        total += 1 / denominator
    
    return f"{total:.2f}"


#

# Examples:
print(series_sum(1))  # "1.00"
print(series_sum(2))  # "1.25"
print(series_sum(5))  # "1.57"