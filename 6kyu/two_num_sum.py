def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []  # no solution (but problem guarantees exactly one)

if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]
    print(two_sum([3, 2, 4], 6))       # Output: [1, 2]
    print(two_sum([3, 3], 6))          # Output: [0, 1]