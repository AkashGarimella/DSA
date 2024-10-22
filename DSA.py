#Problem 1
nums = []
x = int(input("How many elements do you want to enter: "))
for i in range(x):
    y = int(input("Enter the number: "))
    nums.append(y)

min_num = nums[0]  # Initialize with the first element
for j in range(1, len(nums)):  # Start from the second element
    if nums[j] < min_num:
        min_num = nums[j]  # Update min_num if a smaller element is found
        
print("The smallest number is:", min_num)


#Problem 2
nums = [1, 2, 4, 7, 7, 5]
num_set = set(nums)
print(num_set)

# Convert set to list to access elements by index
num_list = list(num_set)
print(num_list[1])  # Access the second element
print(num_list[-2])  # Access the second-to-last element


#Problem 3
nums = [1,1,2,2,2,3,3]
num_set = set(nums)
num_list = list(num_set)
print(num_list)
res = []
for i in range(len(num_list)):
    res.append(num_list[i])
    
n = len(nums) - len(num_list)
for i in range(n):
    res.append("*")
    
print(res)