# # # # range(stop) -> 0 to stop-1
# # # for i in range(5):
# # #     print(i) # 0 1 2 3 4
# # # # range(start, stop)
# # # for i in range(2, 6):
# # #     print(i) # 2 3 4 5
# # # # range(start, stop, step)
# # # for i in range(0, 11, 2):
# # #     print(i) # 0 2 4 6 8 10
# # # count = 1
# # # while count<=5:
# # #     print(count)
# # #     count+=1


# # # search for a number
# # # for n in [2, 4, 6, 8]:
# # #     if n == 5:
# # #         print("Found 5!")
# # #     break
# # # else:
# # #     print("5 is not in the list")c
# # n = int(input("Enter a number to print its multiplication table: "))
# # for i in range(1,11,1):
# #     print(f"{n}*{i}={n*i}")

# counter = 5
# while counter >0:
#     print(counter)
#     counter -=1
#     if counter == 0:
#         print("let's go!")



# • Print the sum of numbers from 1 to 100 using a loop.
# • Print only even numbers from 1 to 20 using continue.
# • Take a number and check if it is prime, using a loop with break

# sum =0
# for i in range(1,101,1):
#     sum += i
# print(sum)

# for i in range(1,21,1):
#     if i%2==0:
#         print(i)
    
nums = int(input("Enter a number to check if it is prime or not: "))
if nums <= 1:
    print(f"{nums} is not a prime number.")
else:
    is_prime = True
    for i in range(2,nums-1):
        if nums%2==0:
            is_prime = False
            break
    

if is_prime:
    print(f"{nums} is a prime number.")
else:
    print(f"{nums} is not a prime number.")


