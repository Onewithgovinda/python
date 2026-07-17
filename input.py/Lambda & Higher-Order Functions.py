def square(x):
 return x ** 2
# the same thing as a lambda
square = lambda x: x ** 2
print(square(5)) # 25
# multiple arguments
add = lambda a, b: a + b
print(add(3, 4)) 

students = [("Amit", 85), ("Neha", 92), ("Ravi", 78)]

students.sort(key=lambda s: s[1])
print(students) # [('Neha',92),('Amit',85),('Ravi',78)]


nums = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, nums))
print(squares) # [1, 4, 9, 16]
# convert strings to integers
strs = ["10", "20", "30"]
ints = list(map(int, strs))
print(ints) # [10, 20, 30]

nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens) # [2, 4, 6]
words = ["hi", "python", "ok", "lambda"]
long = list(filter(lambda w: len(w) > 2, words))
print(long)

from functools import reduce
nums = [1, 2, 3, 4]
# multiply everything together
product = reduce(lambda a, b: a * b, nums)
print(product) # 24 (1*2*3*4)
# sum everything (though sum() is simpler here)
total = reduce(lambda a, b: a + b, nums)
print(total) # 1


# clean a column of price strings into numbers
raw = ["₹100", "₹250", "₹80"]
prices = list(map(lambda p: int(p.replace("₹", "")), raw))
print(prices) # [100, 250, 80]
# keep only passing scores
scores = [45, 82, 33, 91, 67]
passed = list(filter(lambda s: s >= 40, scores))
print(passed) # [45, 82, 91, 67]
# total revenue with reduce
from functools import reduce
revenue = reduce(lambda a, b: a + b, prices)
print(revenue) # 430
