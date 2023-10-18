# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def two_sum(nums, target):
    d = {}
    for idx, n in enumerate(nums):
        diff = target - n
        if diff in d:
            return [d[diff], idx]
        d[n] = idx

two_sum(nums = [2,7,11,15], target = 9)

# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2

# def search_insert(nums, target):
#     left, right = 0, len(nums) - 1
#     while left <= right:
#         mid = left + (right - left) // 2

#         if nums[mid] == target:
#             return mid
        
#         elif nums[mid] < target:
#             left = mid + 1

#         else:
#             right = mid - 1

#     return left


# search_insert(nums = [1,3,5,6], target = 5)

#big O(n)
# def largest(array, value):
#   for item in array:
#     if item > value:
#       return False
#   return True 

# #big O(n)
# def info_dump(customers):
  
#   print('Customer Names:')
#   for customer in customers: 
#     print(customer['name'])
  
#   print('Customer Locations:')
#   for customer in customers: 
#     print(customer['country'])

# #O(1)
# def first_element_is_red(array):
#   return array[0] == 'red' 

# #0(n)2
# def duplicates(array):
#   for index1, item1 in enumerate(array):
#     for index2, item2 in enumerate(array):
#       if index1 == index2:
#         continue
#       if item1 == item2:
#         return True
#   return False

# #O(m * n)
# words = ['chocolate', 'coconut', 'rainbow']
# endings = ['cookie', 'pie', 'waffle']

# for word in words:
#   for ending in endings:
#     print(word + ending)

# #O(n)
# numbers = [1,2,3,4,5,6,7,8,9,10]

# def print_array(array):
#   for item in array:
#     print(item)

# #O(n2)
# # this is insertion sort
# def insertionSort(arr): 
#   for i in range(1, len(arr)): 
#     key = arr[i] 
#     j = i-1
#     while j >=0 and key < arr[j] : 
#       arr[j+1] = arr[j] 
#       j -= 1
#     arr[j+1] = key 

# #O(n2)
# for i in range(len(my_list)):
#   min_idx = i
#   for j in range(i+1, len(my_list)):
#       if my_list[min_idx] > my_list[j]:
#           min_idx = j

#   my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]