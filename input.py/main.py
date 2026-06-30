import math

# / always returns float — even when it divides evenly!
print(10 / 2) # 5.0 (not 5!)
# // floors DOWN — watch with negatives!
print(-7 // 2) # -4 (not -3!)
# % gives remainder — useful for even/odd, last digit
print(17 % 2) # 1 (odd)
print(9876 % 100) # 6 (last digit!)



# 135 minutes = ? hours and ? minutes
hours, mins = divmod(135, 60)
print(hours, mins) # 2, 15



name = input("Enter your name ")
print("your name is :" + name)

a = int(input("enter your vale of a "))
b = int(input("enter your vale of b "))

print("addition " , a+b)
print("subtract " , a - b)
print("multipletion " , a*b)
print("divide " , a/b)
print("mudule " , a%b)

r = int(input("enter your vale of r "))
area = math.pi*r**2
print("are of the circle : " , area)                  

sec = int(input("enter your vale of a "))
min = sec//60
hour = sec//360
print(hour,min)
#Today is Monday. What day is it after 100 days?
days_ahead = 100
remainder = days_ahead % 7
print(remainder) # 2 --> 2 days after Monday = Wednesday!
