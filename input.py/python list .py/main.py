# Empty list
items = []
# List of numbers
marks = [85, 90, 72, 60]
# Mixed data types allowed
mixed = [1, "Rajeev", 3.14, True]
# Using the list() constructor
letters = list("python") # ['p','y','t','h','o','n']
print(items)
print(marks)
print(mixed)
print(letters)



fruits = ["apple", "banana", "cherry", "mango"]
# 0 1 2 3
# -4 -3 -2 -1
print(fruits[0]) # apple
print(fruits[2]) # cherry
print(fruits[-1]) # mango (last item)
print(fruits[-2]) # cherry



nums = [10, 20, 30, 40, 50, 60]
print(nums[1:4]) # [20, 30, 40]
print(nums[:3]) # [10, 20, 30] from start
print(nums[3:]) # [40, 50, 60] till end
print(nums[::2]) # [10, 30, 50] every 2nd
print(nums[::-1]) # [60,50,40,30,20,10] reversed!
# <<<<<<< HEAD


# print(nums[0:7:2])

# =======

# # print(nums[0:7:2])


# >>>>>>> 5b3405a (5 practice solutions in a file video11_2_problems)
tasks = ["code", "test"]
tasks.append("deploy") # ['code','test','deploy']
#tasks.insert(1, "review") # ['code','review','test','deploy']
#tasks.remove("test") # ['code','review','deploy']
last = tasks.pop() # last = 'deploy'
#tasks[0] = "design" # ['design','review']
print(tasks)
print(tasks.append("deploy"))
# print(last)
# print(len(tasks)) # 2
# print("review" in tasks) # True
# print("test" not in tasks) # True
# print(tasks.index("review")) # 1
# print(tasks.count("review")) # 1


matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
print(matrix[0]) # [1, 2, 3]
print(matrix[1][2]) # 6 (row 1, col 2)
print(matrix[2][2])


point = [10, 20, 30,78,89]
x, y, *z = point
print(x, y, z) # 10 20 30

# Star (*) captures the rest
first, *rest = [1, 2, 3, 4, 5]
print(first) # 1
print(rest) # [2, 3, 4, 5]

a = [1, 2, 3]
b = a # WRONG — same list!
print(a) # [1, 2, 3]
b.append(4)
print(a) # [1, 2, 3, 4] a changed too
# Correct ways to copy:
b = a.copy() # method 1
b = a[:] # method 2 (full slice)
b = list(a) # method 3
print(b) # [1, 2, 3, 4]
print(a) # [1, 2, 3, 4]


a =["python", "java", "c++", "rust", "go"]

print(a[0])
print(a[-5])
print(a[-1])
print(a[4])



marks = [45, 67, 89, 23, 90, 56, 78] 
print(marks[0:3]) # [45, 67, 89, 23]
print(marks[5:]) # [23, 90, 56, 78]
print(marks[::2]) # [45, 89, 90, 78]
print(marks[::-1]) # [78, 56, 90, 23, 89, 67, 45]

todos = ["wake up", "study"]
todos.append("exercise")
todos.insert(1,"meditate")
todos.remove("study")
todos[-1]="sleep"
print(todos) # ['wake up', 'meditate', 'sleep']
a = [["raj","jay","van"],[34,45,67]]
print(a[0][1]) # jay
print(a[1][2])

data = [101, "Varanasi", 25.3, 82.9]
id, city, lat, lon = data
print(f"{id}, {city}, {lat}, {lon}")


original = [1, 2, 3]
backup = original.copy() 
print(backup.append(99))
print(backup) # [1, 2, 3, 99]
print(original) # [1, 2, 3]
# <<<<<<< HEAD
# =======


# List of scores
scores = [40, 80, 65, 95, 70]

# Find highest and lowest scores
highest = max(scores)
lowest = min(scores)

# Find the position of the highest score
winner_position = scores.index(highest)

print("Highest score:", highest)
print("Lowest score:", lowest)
print("Winner is at position", winner_position)

ks = [45, 67, 89, 23, 90, 56, 78] 
print(marks[0:3]) # [45, 67, 89, 23]
print(marks[5:]) # [23, 90, 56, 78]
print(marks[::2]) # [45, 89, 90, 78]
print(marks[::-1]) # [78, 56, 90, 23, 89, 67, 45]
# >>>>>>> 5b3405a (5 practice solutions in a file video11_2_problems)
