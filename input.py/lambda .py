# Given nums = [1, 2, 3, 4, 5] , use map() with a lambda to build a list where
# every number is doubled.
# Uses: map + lambda

nums = [1,2,3,4,5]

key = map(lambda a: a * 2, nums)
print(list(key))


# Keep the Positives
# Given nums = [-3, 5, -1, 8, 0, -7, 2] , use filter() with a lambda to keep
# only the positive numbers.
# Uses: filter + lambda

nums = [-3, 5, -1, 8, 0, -7, 2]
key = list(filter(lambda a: a>0 ,nums))
print(key)

# Cube with Lambda
# Write a lambda cube that returns the cube of a number. Test it on 2, 3, and 5.
# Hint: cube = lambda x: x ** 3
key = lambda a:a**3
print(key(3))

# Uppercase All
# Given words = ["python", "lambda", "map"] , use map() to build a list of the
# words in UPPERCASE.
# Hint: map(lambda w: w.upper(), words)
words = ["python", "lambda", "map"]
key = list(map(lambda w : w.upper(),words))
print(key)

# Filter the Odds
# Given numbers 1 to 20, use filter() to keep only the odd numbers.
nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
key = list(filter(lambda a : a%3==0 ,nums))
print(key)

# Sum with reduce
# Using reduce() , find the sum of all numbers in [5, 10, 15, 20] . Then modify it
# to find the maximum instead.
# Hint: for max, reduce(lambda a, b: a if a > b else b, nums) .
from functools import reduce
nums= [5,10,15,20]
key = reduce(lambda a, b: a if a > b else b, nums)
print(key)

# Sort by Last Letter
# Given names = ["Amit", "Neha", "Ravi", "Sara"] , sort them by their last letter
# using sorted() with a lambda key.
# Hint: sorted(names, key=lambda n: n[-1])

names = ["Amit", "Neha", "Ravi", "Sara"]
key = list(sorted(names,key = lambda a:a[-1]))
print(key)

# Clean the Prices
# Given raw = ["$100", "$250", "$99"] , use map() to strip the $ and convert
# each to an integer. Then use filter() to keep only prices above 100.
# Hint: chain map then filter; p.replace("$", "") .
raw = ["$100", "$250", "$99"]
# kay = map(lambda p:int(p.replace("$", ""),raw))
prices = list(map(lambda p: int(p.replace("$", "")), raw))
# print(kay)
filtered_prices = list(filter(lambda p: p > 100, prices))
print(filtered_prices)

# map vs comprehension
# Write the same task — squaring only the even numbers from 1 to 10 — TWO
# ways: once using map + filter , and once using a list comprehension. In a
# comment, say which you find more readable and why.
# Tests: understanding both styles and when each fits
nums = range(1,11)

kay = list(map(lambda a:a**2,filter(lambda a:a%2==0,nums)))
print(kay)

numbers = range(1, 11)

# Square only the even numbers
result = [x ** 2 for x in numbers if x % 2 == 0]

print(result)

# I find the list comprehension more readable because
# it is shorter and easier to understand at a glance.

# Longest Word with reduce
# Given a list of words, use reduce() to find the longest word — without max() .
# ["hi", "python", "lambda", "ok"] → "python" .
# Tests: custom combine step; reduce(lambda a, b: a if len(a) >= len(b) else b,
# words) .


words= ["hi", "python", "lambda", "ok"]
kay = (reduce(lambda a,b:a if len(a)>=len(b) else b,words))
print(kay)