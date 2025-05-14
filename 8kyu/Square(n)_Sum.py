#Input is an array of numbers
#Ouput is squared summation of all the numbers in the array

def square_sum(numbers):
    squared_nums = []
    #your code here
    for i in numbers:
        square_num = i**2
        squared_nums.append(square_num)
    return sum(squared_nums)


#Other solutions
def square_sum(numbers):
    # Calculate the sum of squares using a generator expression
    return sum(x ** 2 for x in numbers)