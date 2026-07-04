# nums = [34, 12, 78, 5, 60]
# smal = nums[0]
# for i in nums:
#     if i < smal:
#         smal = i
# print(smal)
n = int(input("Enter the number "))
count =0
for i in range(1, n+1):
    if n%2==0:
        count+=1
        
print(count)
