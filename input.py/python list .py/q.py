n = int(input("Enter the number "))
prime = True

for i in range(2, n-1):
    if n%i == 0:
        prime = False
        break

if prime:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")
        


items = [1, 2, 2, 3, 4, 4, 4, 5] 
first = items[0]
for i in items:
    if i > first:
        first = i
    

    