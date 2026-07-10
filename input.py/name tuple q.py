
# Create a Book Record
# Create a named tuple Book with fields title , author , year . Make one book
# and print a sentence using field names, like "Wings of Fire by Kalam (1999)" .
# Uses: namedtuple + attribute access

from collections import namedtuple


s1 = namedtuple("book",["title","author","year"])
s2=s1("Wings of Fire","Kalam",1999)
print(f"{s2.title} by {s2.author} ({s2.year})")


# Build from a Row with _make()
# Using the same Book tuple, you have a row ["Ignited Minds", "Kalam", 2002] .
# Use _make() to turn it into a Book, then print the author.
# Uses: _make()

row = ["Ignited Minds", "Kalam", 2002]
book = s1._make(row)
print(book.author) # Kalam

# Point in 2D
# Create a named tuple Point with fields x and y . Make a point (3, 7) and print
# its coordinates using field names.
# Hint: Point = namedtuple("Point", ["x", "y"])

p = namedtuple("point",["x","y"])
point = p(3, 7)
print(f"Point coordinates: ({point.x}, {point.y})") # Point coordinates: (3, 7)



# Record to Dictionary
# Create an Employee named tuple with name , dept , salary . Make one employee,
# then convert it to a dictionary using _asdict() and print it.
# Hint: emp._asdict()

employe = namedtuple("Employee",["name","dept","salary"])
e= employe("John","IT",50000)
emp_dict = e._asdict()  
print(emp_dict) # {'name': 'John', 'dept': 'IT', 'salary': 50000}

# Give a Raise with _replace()
# Using your Employee tuple, create a new record where the salary is increased by
# 5000 using _replace() . Print both the original and the updated record to prove
# the original didn't change.

salary_raise = e._replace(salary=e.salary + 5000)
print(e.salary) # 50000 (original unchanged)

# rint the Field Names
# Create a Movie named tuple with title , director , rating . Print all its field
# names using _fields .
# Hint: Movie._fields
movie = namedtuple("movie",["title","director","rating"])
print(movie._fields) # ('title', 'director', 'rating')


# Rows to Records
# You have a list of rows:
# rows = [["Amit", 21, 8.5], ["Neha", 20, 9.1], ["Ravi", 22, 7.8]]
# Create a Student named tuple ( name , age , gpa ). Loop over the rows, use
# _make() to convert each into a Student, and print each student's name and gpa.
# Hint: loop the rows, call Student._make(row) each time.
stu = namedtuple("student",["name","age","gpa"])
rows = [["Amit", 21, 8.5], ["Neha", 20, 9.1], ["Ravi", 22, 7.8]]

for i in rows:
    student = stu._make(i)
    print(f"{student.name} has a GPA of {student.gpa}")