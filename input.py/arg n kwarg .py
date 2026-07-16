# Sum Any Numbers
# Write a function total(*args) that returns the sum of however many numbers
# are passed. Test it with 2 numbers, 5 numbers, and none.
# Uses: *args

def total(*args):
    print(args)
    return sum(args)


print(total(1,2,3))


# Print a Profile
# Write a function profile(**kwargs) that prints every key-value pair passed to it
# as "key: value" . Call it with a few named arguments.
# Uses: **kwargs + .items()

def profile(**kwargs):
    for key,value in kwargs.items():
        print(key,"=",value)

profile(
    name="Govinda",
    age=20,
    course="B.Tech CSE",
    city="Delhi"

)
print(profile)


# Multiply Everything
# Write a function multiply(*args) that returns the product of all numbers passed.
# multiply(2, 3, 4) → 24.
# Hint: start a result at 1, loop over args , multiply each.
def mul(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(mul(1,2,3,4))

# Count the Arguments
# Write a function how_many(*args) that returns how many arguments were passed.
# Test with different counts.
# Hint: len(args)

def how_many(*args):
    return len(args)

# Test cases
print(how_many())                  # 0
print(how_many(10))                # 1
print(how_many(1, 2, 3))           # 3
print(how_many("a", "b", "c", "d"))# 4
print(how_many(1, 2, 3, 4, 5))     # 5


# Greeting with kwargs
# Write a function describe(**kwargs) that prints "name is Amit" , "age is 21" ,
# etc., for whatever keyword arguments are passed.
# Hint: loop kwargs.items() 

def dec(**kwargs):
    for key , value in kwargs.items():
        print(key,value)



dec(
    name="Amit",
    age=21,
    city="Delhi",
    course="B.Tech"
)

# Max of Many
# Write a function biggest(*args) that returns the largest number passed —
# without using max() . Handle the empty case by returning None .
# Hint: "best so far" pattern from #11.2, looping over args .
def biggest(*args):
    if len(args) == 0:
        return None

    largest = args[0]  # Best so far

    for num in args:
        if num > largest:
            largest = num

    return largest


# Test cases
print(biggest(10, 25, 7, 18))      # 25
print(biggest(5))                  # 5
print(biggest(-2, -8, -1, -5))     # -1
print(biggest())                   # None



# Write a function add3(a, b, c) that returns the sum of three numbers. Then,
# given a list nums = [4, 5, 6] , call add3 by unpacking the list with * .
# Hint: add3(*nums) .

def add3(a, b, c):
    return a + b + c

# List of numbers
nums = [4, 5, 6]

# Unpack the list using *
print(add3(*nums))


# Write a function order(customer, *items, **details) . Print the customer name,
# the list of items, and any extra details (like discount=10 ). Call it with a name,
# several items, and a couple of keyword details.
# Hint: combine positional + *args + **kwargs in the correct order.

def order(customer, *items, **details):
    print("Customer:", customer)

    print("Items:")
    for item in items:
        print("-", item)

    print("Details:")
    for key, value in details.items():
        print(f"{key}: {value}")


# Function call
order(
    "Amit",
    "Pizza",
    "Burger",
    "Cold Drink",
    discount=10,
    payment="Online"
)