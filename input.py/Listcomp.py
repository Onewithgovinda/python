num= [4,5,6,3,2,8,9,5,4,3,6,7,4,3]
num.sort()
print(num)

num= [4,5,6,3,2,8,9,5,4,3,6,7,4,3]
num.sort(reverse=True)
print(num)


n = sorted(num)
print(n)

fruits = ["apple", "banana", "apple", "cherry"] 
print(fruits.index("banana"))
print(fruits.count("apple"))


# Squares of Even Numbers Using a single list comprehension, build a list of the squares of all even numbers from 1 to 20. Expected: [4, 16, 36, 64, 100, 144, 196, 256, 324, 400] Uses: comprehension + filter ( if ) + transform

sq = [i**2 for i in range(1,21) if i%2==0]
print(sq)



# SOLVE IN VIDEO 2

# Sort & Find Position Given scores = [55, 90, 72, 88, 60] : sort it in descending order, then print the position (index) of the score 72 in the sorted list. Uses: sort(reverse=True) + index
scores = [55, 90, 72, 88, 60]
scores.sort(reverse=True)
print(scores)
print(scores.index(72))


# Uppercase the Long Words Given words = ["hi", "python", "ok", "comprehension", "go"] , use a comprehension to build a list of words longer than 2 letters, each in UPPERCASE. Expected: ['PYTHON', 'COMPREHENSION' ] Hint: filter with if len(w) > 2, transform with w.upper().
words = ["hi", "python", "ok", "comprehension", "go"]
upper = [w.upper() for w in words if len(w) > 2]
print(upper)


# Merge & Count You have list1 = [1, 2, 3] and list2 = [3, 4, 1, 5] . Use extend() to merge them into one list, then use count() to print how many times 1 appears in the merged list. Hint: extend() merges, count() counts.
list1 = [1, 2, 3]
list2 = [3, 4, 1, 5]
list1.extend(list2)
print(list1)
print(list1.count(1))

# Flatten the Matrix Given matrix = [[1, 2], [3, 4], [5, 6]] , use a nested comprehension to flatten it into [1, 2, 3, 4, 5, 6] . Hint: [num for row in matrix for num in row] - read it outer to inner.
matrix = [[1, 2], [3, 4], [5, 6]]
f=[num for row in matrix for num in row]
print(f)


# FIzZbuzz as a ComprenensTon Rewrite FizzBuzz (1 to 20) as a single list comprehension that produces a list of strings/numbers. Expected start: [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', ... ] Hint: Use a nested conditional expression: "FizzBuzz" if ... else "Fizz" if ... else .... This is also a great "when it gets ugly" discussion - is the loop version more readable?
fiz=[ "FizzBuzz" if i%15==0 else "Fizz" if i%3==0 else "Buzz" if i%5==0 else i for i in range(1,21)]
print(fiz)

# Common Elements Given a = [1, 2, 3, 4, 5] and b = [3, 4, 5, 6, 7] , use a comprehension to build a list of numbers that appear in both lists. Expected: [3, 4, 5] Hint: [x for x in a if x in b] - read it as "keep x from a if x is also in b".
a = [1, 2, 3, 4, 5] 
b = [3, 4, 5, 6, 7]
common = [x for x in a if x in b]
print(common)

for i in a:
    if i in b:
        print(i)

