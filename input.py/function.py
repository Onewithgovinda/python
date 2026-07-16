# Greet with a Default
# Write a function greet(name, msg="welcome") that prints a greeting. Call it once
# with just a name, and once with both a name and a custom message.
# Uses: def + default arguments

def greet(name, msg="welcome"):
    print(f"{msg}, {name}!")

print("Calling greet with just a name:")
greet("Alice")  # Output: welcome, Alice!


# Rectangle Area
# Write a function area(length, width) that returns the area (not prints). Call it,
# store the result in a variable, and print it.
# Uses: return value

def area(len,wid):
    return len*wid

print(area(5, 10))  # Output: 50


# Is Even?
# Write a function is_even(n) that returns True if n is even, else False . Test it
# with a few numbers.
# Hint: return n % 2 == 0


def even(n):
    return n % 2 == 0
print(even(4))  # Output: True


# Simple Interest
# Write a function interest(principal, rate, years) that returns the simple
# interest ( P * R * T / 100 ). Give rate a default of 5. Call it once using the
# default and once overriding it.
# Hint: return the formula; use a default argument for rate.

def int(p,r=5,t=1   ):
    return p*r*t/100
print(int(1000, 5, 2))  # Output: 100.0



# Greatest of Three
# Write a function biggest(a, b, c) that returns the largest of three numbers —
# without using max() .
def biggest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
print(max(3,4,5))



# Grade from Marks
# Write a function grade(marks) that returns "A", "B", "C", or "Fail" based on the
# marks (your own cutoffs). Test it with a few values.
# Hint: if/elif inside the function, then return the grade string.

def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"
    

# emperature Converter
# Write a function convert(temp, to="F") . If to is "F" it returns
# Celsius→Fahrenheit; if "C" it returns Fahrenheit→Celsius. Use a default argument
# and return the result. Test both directions.
# Hint: C→F is temp * 9/5 + 32 ; F→C is (temp - 32) * 5/9 . Use if/else on to .

def convert(temp, to="F"):
    if to == "F":
        # Celsius → Fahrenheit
        return temp * 9 / 5 + 32
    else:
        # Fahrenheit → Celsius
        return (temp - 32) * 5 / 9


# Test both directions
print(convert(30))        # Celsius to Fahrenheit
print(convert(86, "C"))   # Fahrenheit to Celsius
print(convert(0))         # Celsius to Fahrenheit
print(convert(212, "C"))  # Fahrenheit to Celsius


# Sum and Average Together
# Write a function stats(nums) that returns BOTH the sum and the average as a
# tuple. Call it and unpack the result into two variables in one line, then print them.
# Uses: multiple return + unpacking
def stats(nums):
    total = sum(nums)
    average = total / len(nums)
    return total, average


# Test
numbers = [10, 20, 30, 40, 50]

total, average = stats(numbers)   # Tuple unpacking

print("Sum =", total)
print("Average =", average)

# Documented Area Function
# Write a function area(length, width) that returns the area, with a docstring
# explaining what it does. Then print its docstring using area.__doc__ .
# Uses: return + docstring

def area(length, width):
    """
    Returns the area of a rectangle.
    It multiplies the length and width.
    """
    return length * width


# Call the function
result = area(10, 5)
print("Area =", result)

# Print the docstring
print(area.__doc__)



# Divide with Remainder
# Write a function divide(a, b) that returns BOTH the quotient and the remainder
# as a tuple. Unpack and print them for divide(17, 5) → expected 3 and 2 .
# Hint: return a // b, a % b

def rem(a,b):

    return a//b,a%b

q,r = rem(17,5)

# Min, Max and Average
# Write a function summary(nums) that returns the minimum, maximum, AND
# average — three values as a tuple. Add a docstring. Unpack all three and print
# them.
# Hint: return min(nums), max(nums), sum(nums)/len(nums)

def fun(nums):

    """Unpack all three and print"""
    return max(nums),min(nums),sum(nums)/len(nums)
nums = [3,4,5,2,6,7,8]

max,min,avg=fun(nums)


print(max)
print(min)
print(avg)
print(fun.__doc__)


# Your Own Math Module
# Create a file mymath.py with two functions: add(a, b) and is_prime(n) . In a
# second file main.py , import them and use both. (Prime logic is from #11.2.)
# Hint: from mymath import add, is_prime — keep both files in the same folder.

def add(a, b):
    return a + b


def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

# Test add()
print("Sum =", add(10, 20))

# Test is_prime()
num = 17
print(num, "is prime:", is_prime(num))
