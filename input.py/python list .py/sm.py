# Find the Largest Number (without max())
# Given nums = [23, 67, 12, 89, 45] , find the biggest number without using
# max() .
# Uses: loop · if · comparison · "best so far" pattern


nums = [23, 67, 12, 89, 45]
first = nums[0]
for i in nums:
 if i > first:
  first=i
  
print(first)
    
# Find the Smallest Number (without min())
# Given nums = [34, 12, 78, 5, 60] , find the smallest number without using
# min() .
# Hint: Same "best so far" pattern as largest — just flip the comparison to < .
 

nums = [34, 12, 78, 5, 60]
first = nums[0]

for i in nums:
   if i < first: 
    first =i
print(first)

 

# Count Primes in a Range
# Print all prime numbers between 1 and 50, and count how many there are.
# Hint: Reuse your prime-check logic inside another loop. Combine a loop, the break trick, and an
# accumulator.



n = int(input("Enter the number: "))
count =0
for i in range(2, n):
    
    prime = True
    for j in range(2, i):
        if i%j==0:
            prime = False
            break


    if prime:
        count = count + 1
        print(i)
print(count)       


# Remove Duplicates (keep unique only)
# Given items = [1, 2, 2, 3, 4, 4, 4, 5] , build a new list with each number
# appearing only once. Expected: [1, 2, 3, 4, 5]
# Hint: Loop the list, append to a new list only if it's not in it already.


items = [1, 2, 2, 3, 4, 4, 4, 5]

un=[]
for i in items:
    if i not in un:
        un.append(i)
print(un)

# Second Largest Number
# Given nums = [23, 67, 12, 89, 45] , find the second largest number without
# sorting and without max() . Answer: 67.
# Hint: Track two variables — largest and second_largest — and update both as you loop.

nums = [23, 67, 12, 89, 45]

largest = nums[0]
second_largest = nums[0]

for num in nums:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second largest number:", second_largest)


# Most Frequent Number
# Given items = [3, 1, 3, 2, 3, 1, 2, 3] , find the number that appears the most
# times. Answer: 3 (appears 4 times).
# Hint: Combine the duplicate-counting nested loop with the "best so far" pattern to track the
# highest count.



items = [3, 1, 3, 2, 3, 1, 2, 3]

for i in items:
    count = 0
    for j in items:
        if i == j:
            count += 1
print(f"{i} appears {count} times")
            