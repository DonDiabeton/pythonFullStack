def reverse_list(lst):
    left, right = 0, len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst

#resultados#

assert reverse_list([1, 3, 5]) == [5, 3, 1]
assert reverse_list([7, 2, 8, 4]) == [4, 8, 2, 7]
assert reverse_list([9, 6, 3, 0]) == [0, 3, 6, 9]
assert reverse_list([]) == []

#/////////////////////////////////#
def is_palindrome(word):
    return word == word[::-1]

#resultados#

assert is_palindrome("racecar") == True
assert is_palindrome("hello") == False
assert is_palindrome("level") == True
assert is_palindrome("python") == False
assert is_palindrome("radar") == True

#/////////////////////////////////#
#dar cambio#
def coin(amount):
    coins = [25, 10, 5, 1]
    result = [0, 0, 0, 0]
    
    for i in range(len(coins)):
        result[i] = amount // coins[i]
        amount %= coins[i]
    
    return result

#resultados#    

assert coin(87) == [3, 1, 0, 2]
assert coin(42) == [1, 1, 1, 2]
assert coin(99) == [3, 2, 0, 4]
assert coin(53) == [2, 0, 0, 3]
assert coin(17) == [0, 1, 1, 2]

#/////////////////////////////////#
#factorial recursiva#
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

#resultados#    

assert factorial(5) == 120
assert factorial(4) == 24
assert factorial(0) == 1
assert factorial(1) == 1

#/////////////////////////////////#
#fibonacci recursiva#
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

#resultados#

assert fibonacci(5) == 5
assert fibonacci(4) == 3
assert fibonacci(7) == 13
assert fibonacci(2) == 1