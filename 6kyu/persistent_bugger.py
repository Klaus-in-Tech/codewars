def persistence(n):
    # your code
    count = 0
    while n >= 10:
        product = 1
        for digit in str(n):
            product *= int(digit)
        n = product
        count +=1
    return count

if __name__ == "__main__":
    print(persistence(39))  # Example usage
    