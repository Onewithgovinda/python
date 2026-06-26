# # # # # # # s = "    hello WORLD"
# # # # # # # # Dot notation — call method on the string
# # # # # # # result = s.upper()
# # # # # # # # print(result) # HELLO WORLD
# # # # # # # # print(s) # hello world ← original unchanged!
# # # # # # # # # You can chain methods
# # # # # # # # print(s.strip().title()) # Hello World
# # # # # # # print(s.upper())    
# # # # # # # print(s.lower())    
# # # # # # # print(s.title())    
# # # # # # # print(s.capitalize())  
# # # # # # # print(s.swapcase())  
# # # # # # # print(s.strip())        








# # # # # # # *********************************************************************



# # # # # # s = "Python is fun and Python is powerful"
# # # # # # # find() — index of first match, returns -1 if not found
# # # # # # # print(s.find("Python")) # 0
# # # # # # # print(s.find("Python", 5)) # 18 ← search from index 5 onward
# # # # # # # print(s.find("Java")) # -1 ← not found, NO error
# # # # # # # # index() — same as find() but raises ValueError if not found
# # # # # # # print(s.index("is")) # 7
# # # # # # # # s.index("Java") # ■ ValueError: substring not found
# # # # # # # # count() — how many times does substring appear?
# # # # # # # print(s.count("Python")) # 2
# # # # # # # print(s.count("is")) # 2
# # # # # # # print("banana".count("an")) # 2

# # # # # # # print(s.find("Python",2))

# # # # # # # print(s.find("java"))
# # # # # # # 





# # # # # # # s = "I love Java, Java is great"
# # # # # # # # Replace ALL occurrences by default
# # # # # # # print(s.replace("Java", "Python")) # I love Python, Python is great
# # # # # # # # Replace only first N occurrences
# # # # # # # print(s.replace("Java", "Python", 1)) # I love Python, Java is great
# # # # # # # # Delete a substring (replace with empty string)
# # # # # # # print(s.replace("Java, ", "")) # I love Java is great




# # # # # # # Default split — splits on ANY whitespace
# # # # # # # s = " one two three "
# # # # # # # print(s.split()) # ['one', 'two', 'three'] — also strips spaces!
# # # # # # # # Split on specific separator
# # # # # # # s2 = "one,two,three,four"
# # # # # # # print(s2.split(',')) # ['one', 'two', 'three', 'four']
# # # # # # # # Limit splits with maxsplit
# # # # # # # print(s2.split(',', 2)) # ['one', 'two', 'three,four']
# # # # # # # # Split a sentence into words
# # # # # # # sentence = "Python is awesome"
# # # # # # # words = sentence.split() # ['Python', 'is', 'awesome']
# # # # # # # s = 'one two three'
# # # # # # # # words = s.split()
# # # # # # # # upper_words = [w.upper() for w in words] # (we will cover this later!)
# # # # # # # # result = ' '.join(upper_words)
# # # # # # # result = s.upper()
# # # # # # # print(result) # ONE TWO THREE


# # # # # # # print("hello123".isalnum()) # True — all alphanumeric?
# # # # # # # print("hello".isalpha()) # True — all letters?
# # # # # # # print("12345".isdigit()) # True — all digits?
# # # # # # # print(" ".isspace()) # True — all whitespace?
# # # # # # # print("Hello World".istitle())# True — title case?
# # # # # # # print("HELLO".isupper()) # True — all uppercase?
# # # # # # # print("hello".islower()) # True — all lowercase?
# # # # # # # # startswith / endswith
# # # # # # # print("Python".startswith("Py")) # True
# # # # # # # print("Python".endswith("on")) # True
# # # # # # # print("Python".startswith(("Py","Go"))) # True ← accepts a tuple!



# # # # # # s = "Python"
# # # # # # print(s.center(20)) # " Python "
# # # # # # print(s.center(20, "-")) # "-------Python-------"
# # # # # # print(s.ljust(20, ".")) # "Python.............."
# # # # # # print(s.rjust(20, ".")) # "..............Python"
# # # # # # # zfill — zero-pad number strings
# # # # # # print("42".zfill(5)) # "00042"
# # # # # # print("7".zfill(4)) # "0007"
# # # # # # # Real use — printing formatted table
# # # # # # for item, price in [("Apple",12),("Mango",25),("Banana",8)]:


# # # # # # name = "govinda"
# # # # # # print(f"my name is : {name}")
# # # # # scor= 89
# # # # # print(f"i got this marks : {scor}")


# # # # s = '1234'
# # # # print("hello1234".isalpha())
# # # # print("12345".isdigit())
# # # # print("hello123".isalpha())

# # # # s='This is bad code with bad habits'
# # # # print(s.replace("bad","good"))
# # # s = 'one:two:three'
# # # print(s.split(":"))
# # s = ['Python', 'is', 'fun']
# # print(" ".join(s))
# s = "Python"

# print(s.startswith("Py"))
# print(s.endswith("on"))


# name = "Govinda"

# print(name.rjust(30))
# num = "7"

# print(num.zfill(4))


# x ='govnida'
# y=89.9
# print(f'My name is {x} and my score is {y}')



# s = "PyMaster India"





# s='banana'
# print(s.count("a"))

# data = "Rajeev,25,Varanasi,Python"

# values = data.split(",")
# print(values)


# user_input = "12345"

# if user_input.isdigit():
#     print("Valid Integer")
# else:
#     print("Not Valid")



# s = "PyMaster India"

# print(s.swapcase())    


# s = "a::b::c"

# parts = s.split("::")
# result = " | ".join(parts)

# print(result)

# num = 1234567.89

# print(f"{num:,.2f}")