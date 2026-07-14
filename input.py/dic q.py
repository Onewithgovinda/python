# Student Profile CRUD
# Create a dict student with name and age . Then: add a course key, update the
# age, safely read a missing email key with .get() , and delete the course. Print
# the dict after each step.
# Uses: add, update, get, delete

from collections import Counter, defaultdict
from os import name


student = {"name": "Amit", "age": 21}
print(student) # {'name': 'Amit', 'age': 21}
student["course"] = "CSE"
print(student) # {'name': 'Amit', 'age': 21, 'course': 'CSE'}
student["email"] = "N/A"
print(student.get("email")) # N/A
del student["email"] # This will raise a KeyError since 'email' does not exist
print(student) # {'name': 'Amit', 'age': 21, 'course': 'CSE'}


# Print a Price List
# Given prices = {"pen": 10, "book": 50, "bag": 200} , loop over it with
# .items() and print each line as "pen costs 10" .
# Uses: .items() looping

prices = {"pen": 10, "book": 50, "bag": 200}
for item, price in prices.items():
    if price > 10:
        print(f"{item}: ${price}")

# Phone Book
# Build a phone book dict with 3 name → number entries. Ask the user for a name
# and print the number using .get() so a missing name prints "Not found"
# instead of crashing.
# Hint: book.get(name, "Not found")


# phone  = {989776:"Amit", 989777:"Neha", 989778:"Ravi"}
# name = input("Enter a name: ")
# print(phone.get(name, "Not found"))

# Phone Book Dictionary
book = {
    "Alice": "9876543210",
    "Bob": "9123456780",
    "Charlie": "9988776655"
}

# Ask the user for a name
name = input("Enter the name: ")

# Print the phone number or "Not found"
print(book.get(name, "Not found"))


# Total & Highest
# Given marks = {"math": 90, "sci": 85, "eng": 78} , use looping to print the
# total marks and the subject with the highest marks.
# Hint: loop .values() for the total; loop .items() tracking the best (pattern from #11.2).
marks = {"math": 90, "sci": 85, "eng": 78} 
sum =0
max = 0
for sub,mark in marks.items():
    sum += mark
    if mark > max:
        max = mark
print("Total marks:", sum) # Total marks: 253
print("Maximum marks:", max) # Maximum marks: 90

students = {
    "s1": {"name": "Amit", "gpa": 8.5},
    "s2": {"name": "Neha", "gpa": 9.1},
    "s3": {"name": "Ravi", "gpa": 7.8}
}
for sid,info in students.items():
    print(sid, "->", info["name"], info["gpa"])



# Count Letters with defaultdict
# Take a word from the user. Use defaultdict(int) to count how many times each
# letter appears, and print the result.
# Hint: counts = defaultdict(int) , then counts[ch] += 1 .

counts = defaultdict(int) # missing keys start at 0
word = input("Enter a word: ")
for ch in word:
    counts[ch] += 1

for letter, count in counts.items():
    print(letter, ":", count)



# Word Frequency with Counter
# Take a sentence from the user. Split it into words and use Counter to find the 3
# most common words. Print them with their counts.
# Hint: Counter(sentence.split()).most_common(3)
words = input("Enter a sentence: ")
word_counts = Counter(words.split())
for word, count in word_counts.most_common(3):
    print(word, ":", count)
