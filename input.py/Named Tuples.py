student = ("Amit", 21, "BCA", 8.5)
print(student[0]) # Amit ... but was index 3 gpa or age?
print(student[3]) # 8.5 ... you have to remember!


from collections import namedtuple
# define the shape: a name + its fields
Student = namedtuple("Student", ["name", "age", "course", "gpa"])
# create a record
s = Student("Amit", 21, "BCA", 8.5)
print(s.name) # Amit (access by name!)
print(s.gpa) # 8.5
print(s[0]) # Amit (still works like a tuple)

# fields can also be given as a single space-separated string
Point = namedtuple("Point", "x y")
p = Point(10, 20)
print(p.x, p.y) # 10 20
Student = namedtuple("Student", ["name", "age", "course", "gpa"])
row = ["Neha", 20, "BCA", 9.1]
s = Student._make(row) # turns the list into a Student
print(s.name, s.gpa) # Neha 9.1

s = Student("Amit", 21, "BCA", 8.5)
d = s._asdict()
print(d)
# {'name': 'Amit', 'age': 21, 'course': 'BCA', 'gpa': 8.5}
s = Student("Amit", 21, "BCA", 8.5)
s2 = s._replace(gpa=9.0) 
print(s.gpa) # 8.5 (original unchanged)
print(s2.gpa) # 9.0 (the updated copy)
print(Student._fields)
# ('name', 'age', 'course', 'gpa')
