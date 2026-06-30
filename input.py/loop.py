# # # # # # # range(stop) -> 0 to stop-1
# # # # # # for i in range(5):
# # # # # #     print(i) # 0 1 2 3 4
# # # # # # # range(start, stop)
# # # # # # for i in range(2, 6):
# # # # # #     print(i) # 2 3 4 5
# # # # # # # range(start, stop, step)
# # # # # # for i in range(0, 11, 2):
# # # # # #     print(i) # 0 2 4 6 8 10
# # # # # # count = 1
# # # # # # while count<=5:
# # # # # #     print(count)
# # # # # #     count+=1


# # # # # # search for a number
# # # # # # for n in [2, 4, 6, 8]:
# # # # # #     if n == 5:
# # # # # #         print("Found 5!")
# # # # # #     break
# # # # # # else:
# # # # # #     print("5 is not in the list")c
# # # # # n = int(input("Enter a number to print its multiplication table: "))
# # # # # for i in range(1,11,1):
# # # # #     print(f"{n}*{i}={n*i}")

# # # # counter = 5
# # # # while counter >0:
# # # #     print(counter)
# # # #     counter -=1
# # # #     if counter == 0:
# # # #         print("let's go!")



# # # # • Print the sum of numbers from 1 to 100 using a loop.
# # # # • Print only even numbers from 1 to 20 using continue.
# # # # • Take a number and check if it is prime, using a loop with break

# # # # sum =0
# # # # for i in range(1,101,1):
# # # #     sum += i
# # # # print(sum)

# # # # for i in range(1,21,1):
# # # #     if i%2==0:
# # # #         print(i)
    
# # # nums = int(input("Enter a number to check if it is prime or not: "))
# # # if nums <= 1:
# # #     print(f"{nums} is not a prime number.")
# # # else:
# # #     is_prime = True
# # #     for i in range(2,nums-1):
# # #         if nums%2==0:
# # #             is_prime = False
# # #             break
    

# # # if is_prime:
# # #     print(f"{nums} is a prime number.")
# # # else:
# # #     print(f"{nums} is not a prime number.")

# # # num = int(input("Enter a number to check if it is prime or not: "))
# # # product = 1
# # # for i in range(1,num+1,1):
# # #     product *= i
# # # print(f"The factorial of {num} is: {product}")

# # # n = int(input("Enter the number: "))
# # # original_n = n
# # # sum =0;
# # # while n > 0:
# # #     rem = n%10
# # #     sum = sum + rem**3
# # #     n = n//10

# # # if sum == original_n:
# # #     print(f"{original_n} is an Armstrong number.")
# # # else:
# # #     print(f"{original_n} is not an Armstrong number.")

# # a =0
# # b=1
# # n = int(input("Enter the number of terms in the Fibonacci series: "))
# # for i in range(n):

# #     c = a+b
# #     a=b
# #     b=c
# #     print(b, end=" ")
# #i =1
n= int(input("Enter the number "))
# # while(n+1>0):
# #     if n%i==0:
# #      print(i)
# #     i+=1

# for i in range(n,0,-1) :
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(i):
#          print("*",end="")
#     print()

# rows = 5

# for i in range(rows, 0, -1):
#     for j in range(rows - i):
#         print(" ", end="")
#     for j in range(i):
#         print("*", end="")
#     print()

for i in range(1, n):
    c = 'A'
    for j in range(1, i ):
        print(c, end="")
        c = chr(ord(c) + 1)
    