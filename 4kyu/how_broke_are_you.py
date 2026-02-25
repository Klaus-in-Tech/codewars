def broke_events(expenditures):
    n = len(expenditures)
    i = 0
    count = 0

    while i < n:
        # Check for 7-day streak
        if i + 6 < n and all(expenditures[i + j] <= 10 for j in range(7)):
            count += 1
            i += 7
        # Check for 3-day streak
        elif i + 2 < n and all(expenditures[i + j] <= 7 for j in range(3)):
            count += 1
            i += 3
        # Check for single day
        elif expenditures[i] <= 3:
            count += 1
            i += 1
        else:
            i += 1

    return count


print(broke_events([5, 6, 7, 20, 3]))  # Output: 2