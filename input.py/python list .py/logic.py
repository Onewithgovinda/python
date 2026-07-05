# nums = [34, 12, 78, 5, 60]
# smal = nums[0]
# for i in nums:
#     if i < smal:
#         smal = i
# print(smal)
# n = int(input("Enter the number "))
# count =0

# for i in range(2,n):
#     for i in range(2, int(n**0.5)+1):
#         prime = True
#         if n%i==0:
#           prime = False
#           break
#        # count+=1
    

#     if prime:

#         count+=1

# print(count)

count = 0

print("Prime numbers between 1 and 50:")
num = int(input("Enter the number: "))
count = 0
for i in range(2, num):
    # is_prime = True
   

    # for i in range(2, int(num ** 0.5) + 1):
    #     if num % i == 0:
    #         is_prime = False
    #         break

    # if is_prime:
    #     print(num, end=" ")
    #     count += 1
    if num % i==0:
        count += 1

print("\n\nTotal prime numbers:", count) 

# items = [1, 2, 2, 3, 4, 4, 4, 5]
# duc = []

# for i in items:
#     count = 0
#     for j in items:
#         if i==j:
#             count+=1
#     if count>1 and i not in duc:
#         duc.append(i)

# print(duc)

