def find_uniq(arr):
    # Determine if the first element is the common one or the unique one
    if arr[0] != arr[1]:
        # First two are different, so one of them is unique
        return arr[0] if arr[0] != arr[2] else arr[1]
    
    # First two are equal, so they represent the common value
    common = arr[0]
    for num in arr:
        if num != common:
            return num
        
print(find_uniq([1, 1, 1, 2, 1, 1]))       # 2
print(find_uniq([0, 0, 0.55, 0, 0]))       # 0.55
print(find_uniq([3, 3, 3, 3, 3, 5, 3]))    # 5
print(find_uniq([2, 1, 1, 1, 1]))         # 2