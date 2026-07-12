# literal — the most common way
student = {"name": "Amit", "age": 21, "gpa": 8.5}
# empty dict
empty = {}
# using the dict() constructor
person = dict(name="Neha", city="Varanasi")
print(person) # {'name': 'Neha', 'city': 'Varanasi'}
# from a list of pairs
pairs = dict([("a", 1), ("b", 2)])
print(pairs) # {'a': 1, 'b': 2}

student = {"name": "Amit", "age": 21}
print(student["name"]) # Amit
# print(student["email"]) # KeyError! key doesn't exist
# get() returns None (or a default) instead of crashing
# print(student.get("email")) # None
# print(student.get("email", "N/A")) # N/A
student = {"name": "Amit", "age": 21}
student["gpa"] = 8.5 # ADD a new key
student["age"] = 22 # UPDATE existing key
print(student) # {'name':'Amit','age':22,'gpa':8.5}

student = {"name": "Amit", "age": 22, "gpa": 8.5}
del student["gpa"] # remove a key
age = student.pop("age") # remove AND return the value
print(age) # 22
print(student) # {'name': 'Amit'}

student = {"name": "Amit", "age": 21, "gpa": 8.5}
# keys (default when you loop a dict)
for key in student:
 print(key) # name / age / gpa
# values
for value in student.values():
 print(value) # Amit / 21 / 8.5
# both, using .items() — this is the most useful
for key, value in student.items():
 print(key, "=", value) # name = Amit ...


student = {"name": "Amit"}
print("name" in student) # True
print("email" in student) # False
students = {
 "s1": {"name": "Amit", "gpa": 8.5},
 "s2": {"name": "Neha", "gpa": 9.1}
}
print(students["s1"]["name"]) # Amit

print(students["s1"]["name"]) # Amit
print(students["s2"]["gpa"]) # 9.1
# loop over a nested dict
print(students["s1"]["name"]) # Amit
print(students["s2"]["gpa"]) # 9.1
# loop over a nested dict
for sid, info in students.items():
 print(sid, "->", info["name"], info["gpa"])


nums = [1, 2, 3, 4]
squares = {n: n * n for n in nums}
print(squares) # {1: 1, 2: 4, 3: 9, 4: 16}
# with a filter
prices = {"pen": 10, "book": 50, "bag": 200}
cheap = {k: v for k, v in prices.items() if v < 100}
print(cheap) # {'pen': 10, 'book': 50}

from collections import defaultdict
# count letters — the messy normal-dict way
counts = {}
for ch in "banana":
 if ch in counts:
  counts[ch] += 1
 else:
  counts[ch] = 1
# the clean defaultdict way
counts = defaultdict(int) # missing keys start at 0
for ch in "banana":
    counts[ch] += 1
print(dict(counts)) # {'b': 1, 'a': 3, 'n': 2} 
from collections import Counter
counts = Counter("banana")
print(counts) # Counter({'a': 3, 'n': 2, 'b': 1})
# count words in a list
words = ["a", "b", "a", "c", "a", "b"]
print(Counter(words)) # Counter({'a': 3, 'b': 2, 'c': 1})
# the 2 most common
print(Counter(words).most_common(2)) # [('a', 3), ('b', 2)]