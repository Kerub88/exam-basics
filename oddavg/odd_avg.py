# Create a function called `odd_average` that takes a list of numbers as parameter
# and returns the average value of the odd numbers in the list
# Create basic unit tests for it with at least 3 different test cases

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers2 = [1, 2, 3, 4, 5]

def odd_average(list_of_numbers):
    odd_numbers = 0
    len_of_odds = 0
    for i in list_of_numbers:
        if i % 2 != 0:
            odd_numbers += i
            len_of_odds += 1
    return odd_numbers // len_of_odds

# print(odd_average(numbers2))
