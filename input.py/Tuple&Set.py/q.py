# Remove Duplicates with a Set
# Given nums = [4, 1, 2, 2, 3, 4, 5, 1] , use a set to get only the unique
# numbers, then print how many unique numbers there are.
# Uses: set() + len()
nums = [4, 1, 2, 2, 3, 4, 5, 1]

print(list(set(nums)))

# Unpack a Student Record
# You have a tuple student = ("Amit", 21, "BCA", 8.5) = name, age, course, gpa.
# Unpack it into four variables in one line and print a sentence: "Amit (21) studies
# BCA with GPA 8.5" .
# Uses: tuple unpacking
student = ("Amit", 21, "BCA", 8.5)
name,age,course,gpa = student
print(f"{name} ({age}) studies{course}with gpa {gpa}")



# Common Friends
# Two people's friend lists: a = {"Ravi", "Sara", "Deep", "Amit"} and b =
# {"Sara", "Amit", "Neha"} . Print their common friends and all friends combined.
# Hint: intersection ( & ) for common, union ( | ) for combined.
a = {"Ravi", "Sara", "Deep", "Amit"} 
b = {"Sara", "Amit", "Neha"}
print(a&b)
print(a|b)

# Swap Without a Temp Variable
# Take two numbers from the user and swap their values using tuple unpacking (no
# third variable). Print before and after.
# Hint: a, b = b, a

a = 1
b=2
a,b = b,a
print(a,b)
# Unique Words Counter
# Take a sentence from the user. Split it into words and print how many unique
# words it contains (ignore repeats).

sentence = input("Enter a sentence: ")

words = sentence.split()

unique_words = set(words)

print("Unique words:", unique_words)
print("Number of unique words:", len(unique_words))


# Who Dropped Out? registered = {"A", "B", "C", "D", "E"} signed up, but attended = {"A", "C", "E"} showed up. Use set difference to find who did NOT attend. Hint: registered - attended
registered = {"A", "B", "C", "D", "E"}
attended = {"A", "C", "E"}
drop = registered - attended
print("Students who did not attend:", drop)


# List vs Set Speed Test
# Create a list and a set both containing numbers 0 to 999999. Check if 999999 is
# present in each. Using the time module, measure and compare how long each
# lookup takes. Explain the result in a comment.
# Hint: import time , record time.time() before and after each lookup. You'll see the O(1) vs
# O(n) difference for rea


import time

# Create a list and a set with numbers from 0 to 999999
numbers_list = list(range(1000000))
numbers_set = set(range(1000000))

# -------- List Lookup --------
start = time.time()

999999 in numbers_list

end = time.time()

print("List lookup time:", end - start, "seconds")

# -------- Set Lookup --------
start = time.time()

999999 in numbers_set

end = time.time()

print("Set lookup time:", end - start, "seconds")

# Explanation:
# List lookup takes O(n) time because it checks elements one by one.
# Set lookup takes O(1) average time because sets use a hash table,
# allowing direct access to the element.