# def reverse(array, i, j):
#     while i < j:
#         array[i], array[j] = array[j], array[i]
#         i += 1
#         j -= 1
#     return array

# def rotate(k: int, array: list[int]):
#     size = len(array) - 1
#     for _ in range(k):
#         reverse(array, 0, size)
#         reverse(array, 1, size)
#     return array
    
# print(rotate(2, [1,2,3,4,5]))


# Running sum
# def running_sum(array):
#     i = 1
#     while i<len(array):
#         array[i] = array[i-1] + array[i]
#         i+=1
#     return array

# print(running_sum([1,2,3,4]))

# def find_product(array, ignore_index: int):
#     i = 0
#     num = 1
#     while i < len(array):
#         if i == ignore_index:
#             i+=1
#             continue
#         num *= array[i]
#         i+=1
#     return num

# # # find_product([1,2,3,4], 2)
# def product_arrayself(array):
#     main_array = []
#     i = 0
#     while i < len(array):
#         main_array.append(find_product(array, i))
#         i+=1
#     print(main_array)
# product_arrayself([1,2,3,4])

# def cumulative_sum(array, type):
#     main_array = []
#     num = 1
#     if type == "left":
#         i = 1
#         main_array.append(1)
#         while i < len(array):
#             num *= array[i-1]
#             main_array.append(num)
#             i+=1
#         return main_array
#     else:
#         i = len(array) - 2
#         main_array.append(1)
#         while i > -1:
#             num *= array[i+1]
#             main_array.append(num)
#             i-=1
#         return reverse(main_array, 0, len(main_array) - 1)

# array = [1,2,3,4]
# print(cumulative_sum(array, "left"))
# print(cumulative_sum(array, "right"))


# array = [-2 ,1, -3 ,4 , -1, 2, 1, -5, 4]

## Kadane for max subarray
# overall_max = float("-inf")
# curr_sum = 0

# i = 0
# while i < len(array):
#     curr_sum += array[i]
    
#     overall_max = max(curr_sum, overall_max)
#     if (curr_sum < 0):
#         curr_sum = 0
#     i+=1
# print(overall_max)

# Modifiend kadane algorithm for max subarray
# overall_min = float("inf")
# curr_sum = 0

# i = 0
# while i < len(array):
#     curr_sum += array[i]
    
#     overall_min = min(curr_sum, overall_min)
#     if (curr_sum > 0):
#         curr_sum = 0
#     i+=1

# print(overall_min)

# maximum subarray custom implementation
# j = 1
# max_sum = 0
# sums = array[0]

# while j < len(array):
    
#     if sums + array[j] < array[j]:
#         sums = array[j]
#     else:
#         sums += array[j]
    
#     if max_sum < sums:
#         max_sum = sums
#     j+=1

# print(max_sum)

# Sort 0s and 1s, Other way is counting but this also works. Its longer than Just size of array. i and j move one by one in each iteration new technique
# array = [0,0,1,0,1,0,0,1,1,1]
# i = 0
# j = len(array) - 1

# while i < j:
#     if array[i] == 1:
#         i += 1
#     elif array[j] == 0:
#         j -= 1
#     else:
#         array[i], array[j] = array[j], array[i]
# print(array)

# Move Zeroes
# array = [7,0,8,5,0,5,8,0]
# array = [2,1]
# array = [0]
# array = [4,2,4,3,5,1,0,0,0,0]
# i = 0
# j = 1
# while j < len(array):
#     if array[i] != 0:
#         i+=1
#         j+=1
#     elif array[j] == 0:
#         j+=1
#     else:
#         array[i], array[j] = array[j], array[i]
#         i+=1
#         j+=1

# print(array)

# Merge sorted arrays
# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3

# m = m - 1 # Treat as i
# n = n - 1 # Treat as l
# k = len(nums1) - 1

# while n > -1:
#     if nums2[n] > nums1[m]:
#         nums1[k] = nums2[n]
#     else:
#         temp_i = m
#         while temp_i > -1:
#             nums1[temp_i + 1] = nums1[temp_i]
#             if nums1[temp_i] < nums2[n]:
#                 break
#             temp_i -= 1
#         nums1[temp_i + 1] = nums2[n]
#         m += 1

#     n-=1
#     k-=1

# print(nums1)


# class Stack:
#     def __init__(self, size) -> None:
#         self.stack = [None for x in range(size)]
#         self.size = size
#         self.top = -1
    

#     def is_full(self):
#         if self.top == self.size:
#             return True
#         return False
    
#     def is_empty(self):
#         if self.top == -1:
#             return True
#         return False
    
#     def push(self, element):
#         if not self.is_full():
#             self.stack[self.top + 1] = element
#             self.top += 1
#             return True
#         return False
    
#     def get_top(self):
#             if not self.is_empty():
#                 return self.stack[self.top]
#             return None
#     def get_size(self):
#         if not self.is_empty():
#             return self.top + 1
#     def pop(self):
#         if not self.is_empty():
#             self.top -= 1
#             return True
#         return False
    
# stack = Stack(10)
# p = "abcd"
# s = "abcd"

# length = len(p)
# if len(s) > len(p):
#     length = len(s)

# i = 0
# while i<length:
#     temp_1,temp_2 = None, None
#     if i < len(p):
#         temp_1 = p[i]            
#         stack.push(p[i])

#     if i < len(s):
#         temp_2 = s[i]    
#         stack.push(s[i])

#     if temp_1 == temp_2:
#         stack.pop()
#         stack.pop()
#     i+=1


# i = 0
# while i <= stack.top:
#     print(stack.stack[i])
#     i += 1


# def matrix(mat:list[list[int]], size, curr=0):
#     if curr == size - 1:
#         return mat
#     for x in range(curr, size):
#         mat[curr][x], mat[x][curr] = mat[x][curr], mat[curr][x]
    
#     mat = matrix(mat, size, curr + 1)
#     if curr == 0:
#         [x.reverse() for x in mat]
#     return mat 

# mat = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
#     ]  

# print(matrix(mat, size=3))

# Next Permutation
# def mergeSort(array, low, high):
#     if low == high:
#         return [array[low]]
    
#     mid = (low + high) // 2
#     left= mergeSort(array, low, mid)
#     right = mergeSort(array, mid + 1, high)

#     i,j = 0,0
#     some = []
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             some.append(left[i])
#             i+=1
#         else:
#             some.append(right[j])
#             j += 1
            
#     while i < len(left):
#         some.append(left[i])
#         i+=1
#     while j < len(right):
#         some.append(right[j])
#         j+=1
#     return some

# print(mergeSort([4,3,6,2,1], 0, 4)) 
# def permu(array):
#     i = len(array) - 1
#     while array[i-1] > array[i]:
#         i-=1
#     p = 0
#     if i > 0:
#         p = i-1

#     temp_i = i
#     mins = i
#     while temp_i < len(array):
#         if array[temp_i] < array[mins] and array[temp_i] > array[p]:
#             mins = temp_i
#         temp_i += 1

#     array[p], array[mins] = array[mins], array[p]
#     print(array)    
  
    # temp_arr = array[i:len(array)]
    # temp_arr.sort()
    # temp_arr = array[0:i] + temp_arr
    # array = temp_arr

# array = [3,2,1]
# permu(array)

# print(array)


# def setCol0(mat, column):
#     for arr in mat:
#         arr[column] = 0

# mat = [
#     [0,1,2,0],
#     [3,4,5,2],
#     [1,3,1,5]
#     ]

# R = len(mat)
# C = len(mat[0])
# for arr in mat:
#     remove = False
#     for i in range(C):
#         if arr[i] == 0:
#             arr[i] = None
#             remove = True
#     if remove:
#         for i in range(C):
#             if arr[i] != None:
#                 arr[i] = 0

# for arr in mat:
#     for i in range(C):
#         if arr[i] == None:
#             setCol0(mat, i)

# print(mat)

# array = [-2 ,1, -3 ,4 , -1, 2, 1, -5, 4]

# curr_sum = 0
# max_so_far = float("-inf")

# for element in array:
#     curr_sum += element
#     max_so_far = max(max_so_far, curr_sum)

#     if curr_sum < 0:
#         curr_sum = 0

# print(max_so_far)


# Binary Search Recursion
# def binary_search(array:list[int], low:int, high:int, target:int):
#     if low > high:
#         return -1
    
#     mid = (low + high) // 2

#     if array[mid] == target:
#         return mid
#     elif array[mid] > target:
#         return binary_search(array, low, mid -1, target)
#     elif array[mid] < target:
#         return binary_search(array, mid+1, high, target)
    

# def binary_search(array:list[int], low:int, high:int, target:int):
    
#     while low <= high:
#         mid = (low + high) // 2

#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             high = mid - 1
#         elif array[mid] < target:
#             low = mid + 1
    
#     return -1


# def special_binary_search(array:list[int], low:int, high:int, size:int):

#     mid = (low + high) // 2

#     if low > high or mid == size - 1:
#         return -1

#     if array[mid] < array[mid+1]:
#         return mid
#     elif array[mid] == 0:
#         return special_binary_search(array, mid + 1, high, size)
#     elif array[mid] == 1:
#         return special_binary_search(array, low, mid - 1, size)


# print(special_binary_search([0,0,0,0,0,0,0], 0, 6, 7))


# machines, products = 3,7
# array = [3,2,5]

# temp_arr = list(array)
# time = 0

# while products > 0:
#     mins = 0
#     for i in range(len(temp_arr)):
#         if (temp_arr[i] - time) < (temp_arr[mins] - time):
#             mins = i

#     time += temp_arr[mins] - time

#     temp_arr[mins] += array[mins]
#     products -= 1

# print(time)


# 3 SUM

# array = [-1,0,1,2,-1,-4]
# array = [-2, 0, 1, 1, 2]
# array = [0,1,1]
# array = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
# array.sort()

# storage = []

# for i in range(len(array)):
#     if i > 0 and array[i] == array[i-1]:
#         continue
#     target = (array[i]) * -1
#     l = i + 1
#     k = len(array) - 1
#     while l < k:
#         if (array[l] == array[l - 1] and l-1 > i) or (array[l] + array[k] < target):
#             l += 1
#         elif  (k <= (len(array)-2) and array[k] == array[k + 1]) or array[l] + array[k] > target:
#             k -= 1
#         elif array[l] + array[k] == target:
#             temp_arr = [array[i], array[l], array[k]]
#             storage.append(temp_arr)
#             l+=1

# print(storage)

# min search in rotated array

# def binary_search(array, low, high, mins=0):
#     if low > high:
#         return array[mins]
#     mid = (low + high) // 2
#     if array[mid] < array[mins]:
#         mins = mid
    
#     if array[low] < array[mid] or array[high] < array[mid]:
#         if array[low] < array[mid] and array[high] < array[mid]:
#             if array[low] < array[high]:
#                 return binary_search(array, low, mid - 1, mins)
#             else:
#                 return binary_search(array, mid+1, high, mins)
#         elif array[low] < array[mid]:
#             return binary_search(array, low, mid-1, mins)
#         else:
#             return binary_search(array, mid+1, high, mins)
#     else:
#         return binary_search(array, low, mid-1,mins)

# Search in Rotated array below
# def bs(arr, l, h, targ) -> int:
#     if l > h:
#         return -1

#     mid = (l + h) // 2

#     if arr[mid] == targ:
#         return mid

#     if arr[mid] <= arr[h]:
#         if arr[mid] < targ <= arr[h]:
#             return bs(arr, mid + 1, h, targ)
#         else:
#             return bs(arr, l, mid - 1, targ)
#     else:
#         if arr[l] <= targ < arr[mid]:
#             return bs(arr, l, mid - 1, targ)
#         else:
#             return bs(arr, mid + 1, h, targ)

# sqrt using binary search

# def bs(target, low, high, prev_mid):
#     if low > high:
#         return prev_mid

#     mid = (low + high) // 2
#     if mid * mid == target:
#         return mid
#     elif mid * mid > target:
#         return bs(target, low, mid-1, prev_mid)
#     else:
#         prev_mid = mid
#         return bs(target, mid+1, high, prev_mid)

# print(bs(9, 1, 9, 0))


# Matrix

# R = int(input())
# C = int(input())

# mat = []
# for x in range(R):
#     temp = [0*y for y in range(C)]
#     mat.append(temp)
# i=0
# while i < R:
#     l = 0
#     while l < C:
#         mat[i][l] = int(input())
#         l+=1
#     i+=1

# print(mat)

# mat = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# i = 0
# while i < len(mat):
#     if i % 2 == 0:
#         l = 0
#         while l < len(mat[i]):
#             print(mat[i][l], end=" ")
#             l+=1
#     else:
#         l = len(mat[i]) - 1
#         while l >= 0:
#             print(mat[i][l], end=" ")
#             l-=1
#     i+=1


# mat = [
#     [1,2,3,44],
#     [4,5,6,77],
#     [7,8,9,88]
# ]

# i = 0
# while i < len(mat[0]):
#     if i % 2 == 0:
#         l = 0
#         while l < len(mat):
#             print(mat[l][i])
#             l+=1
#     else:
#         l = len(mat) - 1
#         while l >= 0:
#             print(mat[l][i])
#             l-=1
#     i+=1

# def reverse(arr):
#     i = 0
#     j = len(arr) - 1

#     while i < j:
#         arr[i],arr[j] = arr[j],arr[i]
#         i+=1
#         j-=1
#     # return arr

# def transpose(mat, size, curr=0):
#     if curr == size-1:
#         return mat
    
#     i = curr
#     while i < size:
#         mat[curr][i], mat[i][curr] = mat[i][curr], mat[curr][i]
#         i+=1
    
#     mat = transpose(mat, size, curr+1)
    
#     return mat

# mat = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# for arr in transpose(mat, len(mat)):
#     reverse(arr)

# print(mat)


# def reverse(array:str, i, j):
#     array = [x for x in array]
#     while i < j:
#         array[i], array[j] = array[j], array[i]
#         i += 1
#         j -= 1
#     return ''.join(array)

# print(reverse("shlf", 0, 0))

# Find pivot integer

# def mod_bin_search(mid, total):
#     left_side = (mid*(mid+1)) // 2
#     right_side = ((total*(total+1)) // 2) - (((mid-1)*(mid-1+1)) // 2)
#     if left_side == right_side:
#         return mid
#     elif left_side > right_side:
#         if mid == mid:
#             return -1
#         else:
#             return mod_bin_search((mid - 1), total)
#     elif left_side < right_side:
#         if (mid + total) // 2 == mid:
#             return -1
#         else:
#             return mod_bin_search((mid + total) // 2, total)

# def mod_bin_search(mid, total):
#     left_side = (mid * (mid + 1)) // 2
#     right_side = ((total * (total + 1)) // 2) - (((mid - 1) * (mid - 1 + 1)) // 2)

#     if left_side == right_side:
#         return mid
#     elif left_side > right_side:
#         if mid <= 1:
#             return -1
#         else:
#             return mod_bin_search((mid - 1)//2 if (mid - 1) % 2 == 1 else (mid - 1)//2 + 1, total)
#     elif left_side < right_side:
#         if mid + total >= total * 2:
#             return -1
#         else:
#             return mod_bin_search((mid + total) // 2 if (mid + total) % 2 == 1 else (mid + total) // 2 + 1, total)

# Example usage
# result = mod_bin_search(5, 10)
# print(result)

# print(mod_bin_search(6, 12))

# def isPalindrome(newstring):
#     string = [x for x in newstring]
#     i = 0
#     j = len(string) - 1

#     while i < j:
#         string[i], string[j] = string[j] , string[i]
#         i+=1
#         j-=1
    
#     if ''.join(string) == newstring:
#         return True

#     return False



# def prints(string, i , j):
#     new_str = ""
#     while i <= j:
#         new_str += string[i]
#         i+=1
#     return new_str

# i = 1
# string = "aaaba"
# while i <= len(string):
#     temp_i = 0
#     j = i - 1

#     while j < len(string):
#         shabd = prints(string, temp_i, j)
#         if isPalindrome(shabd):
#             print(shabd)
#         temp_i += 1
#         j+=1
#     i+=1

# def printAllSubstrings(s, n):
 
#     for i in range(n):
#         temp=""
#         for j in range(i,n):
#             temp+=s[j]
#             print(temp)
 
# printAllSubstrings("aaaba", 5)

# def n_sum(n: int):
#     if n == 0:
#         return 0
    
#     return n + n_sum(n-1)

# def print_n(n: int):
#     if n == 1:
#         print(1)
#         return 
    
#     print(n)
#     print_n(n-1)
#     print(n)

# print_n(5)

# def sum_arr(array,i,length, sum):
#     sum += array[i]

#     if i == length:
#         return sum
#     return sum_arr(array, i+1, length, sum)

# def sum_arr(array, i, length):
#     if i == length:
#         return array[i]
    
#     x = sum_arr(array, i+1, length)

#     return array[i] + x

# array = [1,2,3,4,5]

# print(sum_arr(array, 0, len(array)-1))

# nums = [1,0,1,0,1]
# goal = 2

# sums = 0
# totalis = 0
# i = 0
# j = 1
# totalis += nums[i]
# totalis += nums[j]
# while j <= len(nums) - 1:
#     print(nums[i], nums[j], totalis)
#     if totalis < goal:
#         j+=1
#         totalis += nums[j]
#     elif totalis > goal:
#         totalis -= nums[i]
#         i+=1
#     elif totalis == goal:
#         sums += 1
#         j+=1
#         totalis += nums[j]

# print(sums)
        
# array = [0,0,1,0,0,0,1,1]
# zeros = []
# ones = []

# prev_zeroes = 0
# prev_ones = 0

# for x in array:
#     if x == 0:
#         prev_zeroes += 1
#     else:
#         prev_ones += 1
    
#     zeros.append(prev_zeroes)
#     ones.append(prev_ones)

# i = len(array) - 1
# print(zeros,ones, sep="\n")
# while i >= 0:
#     if zeros[i] == ones[i]:
#         print(i+1)
#         break
#     i-=1
# def reverse(array, i, j):
#     while i < j and i >= 0:
#         array[i], array[j] = array[j], array[i]
#         i += 1
#         j -= 1
#     return array


# array = [3,1,1,1,2,2]
# array = [3,4,5,1,2]
# array = [2,1,3,4]

# mins = 0
# for i in range(len(array)):
#     if array[i] < array[mins]:
#         mins = i

# reverse(array, mins, len(array)-1)
# reverse(array,0, mins-1)
# reverse(array, 0, len(array)-1)

# valid=True
# for i in range(1,len(array)):
#     if array[i] < array[i-1]:
#         valid=False
#         break 
# if valid:
#     print(True)
# else:
#     print(False)


# def sortedArray(a, b):
#     i = 0
#     j = 0
#     arr = []

#     while i < len(a) and j < len(b):
#         if a[i] < b[j]:
#             if len(arr) == 0:
#                 arr.append(a[i])
#             elif len(arr) != 0 and arr[len(arr)-1] != a[i]:
#                 arr.append(a[i])
#             i+=1
#         elif b[j] <= a[i]:
#             if len(arr) == 0:
#                 arr.append(b[j])
#             elif len(arr) != 0 and arr[len(arr)-1] != b[j]:
#                 arr.append(b[j])
#             j+=1

#     while i < len(a):
#         if arr[len(arr)-1] != a[i]:
#             arr.append(a[i])
#         i+=1
#     while j < len(b):
#         if arr[len(arr)-1] != b[j]:
#             arr.append(b[j])
#         j+=1

#     return arr

# print(sortedArray([1, 2, 3, 4, 6], [2, 3, 5]))


# array = [3,3,3,3,3]
# array = [3,1,3,4,2]

# def count(array, num):
#     x = 0
#     for ele in array:
#         if ele <= num:
#             x+=1
#     return x 

# best = None
# low = 1
# high = len(array)-1
# while low <= high:
#     mid = (low + high) // 2

#     if count(array, mid) > mid:
#         best = mid
#         high = mid - 1
#     else:
#         low = mid + 1

# print(best)
    


# def longestSubarrayWithSumK(arr, k):
#     i = 0 
#     j = 0
#     count = 0
#     sums = 0
#     while j <= len(arr):
#         if sums < k:
#             sums += arr[j] if j < len(arr) else 0
#             j+=1
#         elif sums == k:
#             if (j - i) > count:
#                 count = (j - i)
#             sums += arr[j] if j < len(arr) else 0
#             j+=1 
#         elif sums > k:
#             sums -= arr[i]
#             i+=1
#     print(count)
    
# longestSubarrayWithSumK([1,2,1,3])



# array = [1]

# i = 0
# while i < len(array):
#     if array[i] > 0:
#         count = array[i]
#         array[i] = 0
#         while count > 0:
#             if array[count-1] > 0:
#                 temp = array[count-1]
#                 array[count-1] = -1
#                 count = temp
#             else:
#                 array[count-1] -= 1
#                 count = -1
#     i+=1
# new_arr =[]
# for i in range(len(array)):
#     if array[i] == -2:
#         new_arr.append(i+1)
# print(new_arr)

# array = [10,5,2,6]
# array = [10,9,10,4,3,8,3,3,6,2,10,10,9,3]
# array = [1,2,3]
# k = 19
# i, j = 0,1

# prod = array[i] * array[j]
# counts = 0

# while j < len(array)+1:
#     if prod < k:
#         counts += 1
#         j += 1
#         if j < len(array):
#             prod *= array[j]
#     else:
#         if i+1 == j:
#             j += 1
#             i += 1
#             if j < len(array): 
#                 prod = array[i] * array[j] 
#         else:
#             prod //= array[i]
#             i += 1
# i = 0
# while i < len(array):
#     if array[i] < k:
#         counts += 1
#     i+=1
# print(counts)

# def sum(array, length):
#     if length == 0:
#         return array[length]
    
#     return array[length] + sum(array, length-1)

# def sortes(array, length, i):
#     if i == length-1:
#         if array[i] < array[i + 1]:
#             return True
#         else:
#             return False
     
#     bools = sortes(array, length, i+1)

#     if bools == True:
#         if array[i] > array[i + 1]:
#             bools = False
#     return bools

# array = [7,1,5,3,6,4]
# array = [1,2,3,4,5,6]
# array = [1,2,5,4,2,3]
# length = len(array) - 1

# print(sortes(array, length, 0))

# def sort_kar(array, i):
#     if i == len(array)-1:
#         return [array[i]]
    
#     new_arr = sort_kar(array, i+1)

    
#     l = 0
#     is_sort = False
#     while l < len(new_arr):
#         if new_arr[l] > array[i]:
#             new_arr.insert(l,array[i])
#             is_sort = True
#             break
#         l+=1
    
#     if is_sort== False:
#         new_arr.insert(len(new_arr), array[i])
    
#     return new_arr

# array = [7,1,5,3,6,4]

# print(sort_kar(array, 0))

# def coin_kar(n):
#     if n == 1:
#         return ["H", "T"]
    
#     array = coin_kar(n-1)
#     new_arr = []

#     for ele in array:
#         new_arr.append(ele+"H")
#         new_arr.append(ele+"T")
    
#     return new_arr

# print(coin_kar(4))


# def sub_sequence(string, length):
#     if length == len(string)-1:
#         return [' ', string[length]]
    
#     given_arr = sub_sequence(string, length + 1)
#     new_arr = []
    
#     for x in given_arr:
#         new_arr.append(x)
#         new_arr.append(string[length]+x)
#     return new_arr


     

# strings = "abc"
# length = 0

# print(sub_sequence(strings, length))

# longest subarray with elements frequency less than k
# array = [5,5,5,5,5,5,5]
# k = 4


# i, j = 0,0
# count = 0
# hashmap = {}
# while j < len(array):
#     if hashmap.get(array[j], None) == None:
#         hashmap[array[j]] = 1
#     else:
#         hashmap[array[j]] += 1
    
#     while hashmap[array[j]] > k:
#         hashmap[array[i]] -= 1
#         i+=1

#     if (j - (i - 1)) > count:
#         count =  j - (i - 1)

#     j+=1
# print(count)


# majority element

# array = [2,2,1,1,1,2,2]

# element = array[0]
# count = 1
# i = 1
# while i < len(array):
#     if array[i] == element:
#         count += 1
#     else:
#         count -= 1
    
#     if count == 0:
#         element = array[i+1]
#         i+=1
#         count = 1

#     i+=1
# print(element)


# def stairs(n, path):
#     if n == 0:
#         print(path)
#         return
#     if n < 0:
#         return 
    
#     stairs(n-1, path+'1')
#     stairs(n-2, path+'2')
# stairs(38,"")
    


# count = 0
# def mat(curr_row, curr_col, dest_row, dest_col, path):
#     global count
#     if curr_col == dest_col and curr_row == dest_row:
#         print(path)
#         count+=1
#         return 
#     elif curr_col > dest_col or curr_row > dest_row:
#         return

#     mat(curr_row, curr_col+1, dest_row, dest_col,path+"R")
#     mat(curr_row+1, curr_col, dest_row, dest_col,path+"D")

# mat(0,0,2,6,"")
# print(count)


# Best time to buy and sell stocks <- The below is middle okaish approach, Better approach does exist

# def del_binary_search(array:list, low, high, target):
    
#     if low > high:
#         return -1
    
#     mid = (low + high) // 2

#     if array[mid] == target:
#         array.__delitem__(mid)
#     elif array[mid] > target:
#         return del_binary_search(array, mid+1,high, target)
#     else:
#         return del_binary_search(array, low, mid-1, target)

# array = [7,1,5,3,6,4]

# sorted_array = array.copy()
# sorted_array.sort(reverse=True)

# # del_binary_search(sorted_array, 0, len(sorted_array)-1, 4)
# maxs = 0
# for element in array:
#     del_binary_search(sorted_array, 0, len(sorted_array)-1, element)
#     if sorted_array and sorted_array[0] - element > maxs:
#         maxs = sorted_array[0] - element
# print(maxs)

# array = [1,3,2,3,3]
# array = [1,4,2,1]
# k = 3
# freq_of_maxs = 0
# count = 0
# i,j=0,0

# maxs = max(array)

# while j < len(array):
#     if array[j] == maxs:
#         freq_of_maxs += 1
    
#     while freq_of_maxs == k:
#         count += len(array) - j

#         if array[i] == maxs:
#             freq_of_maxs -= 1
#         i+=1

#     j+=1
# print(count)

# Subarrays with K Different Integers
# def retus(array, k):

#     i,j = 0,0
#     count = 0
#     prev_j = None
#     unique_elements = dict()

#     while j < len(array):
#         if unique_elements.get(array[j], None) == None and prev_j != j:
#             unique_elements[array[j]] = 1
#         elif prev_j != j:
#             unique_elements[array[j]] += 1
#         prev_j = j
        
#         if len(unique_elements) <= k:
#             count += j - (i - 1)
#             j+=1
#         else:
#             unique_elements[array[i]] -= 1

#             if unique_elements[array[i]] == 0:
#                 del unique_elements[array[i]]
            
#             i+=1

#     return count

# print(retus(array = [1,2,1,2,3], k = 1))


# Longest consecutive elements

# array = [100,4,200,1,3,2]
# array = [100,101,102,103,104]
# array = [0,3,7,2,5,8,4,6,0,1]
# array = [0]
# hashmap = set(array)

# count = 0
# for x in hashmap:
#     if x-1 not in hashmap:
#         temp_count = 0
#         next_element = x + 1
#         while next_element in hashmap:
#             temp_count += 1
#             next_element = next_element + 1
#         if temp_count + 1 > count:
#             count = temp_count+1

# print(count)


# No think valid paranthesis ques
# def paranthesis_is_valid_stack(string):
#     stack = []
#     size = -1
#     for paranth in string:
#         if paranth == ")":
#             if size > -1 and stack[len(stack)-1] == "(":
#                 stack.pop()
#                 size-=1
#             else:
#                 stack.append(")")
#                 size += 1
#         else:
#             stack.append(paranth)
#             size+=1
    
#     if size == -1:
#         return True
#     else:
#         return False

    
# mat = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# mat = [
#     [1,2,3 ,4 ,5],
#     [4,5,6, 7, 8],
#     [7,8,9, 10, 11]
# ]


# low = 0
# high = len(mat[0])-1

# low_low = 0
# high_high = len(mat)-1

# i = 0
# while high_high >= low_low and high >= low:
#     if i % 4 == 0:
#         for l in range(low, high+1):
#             print(mat[low_low][l])
#         low_low += 1
#     elif i%4 == 1:
#         for l in range (low_low, high_high+1):
#             print(mat[l][high])
#         high -= 1
#     elif i % 4 ==2:
#         for l in range(high, low-1, -1):
#             print(mat[high_high][l])
#         high_high -= 1
#     elif i % 4 == 3:
#         for l in range(high_high, low_low-1, -1):
#             print(mat[l][low])
#         low+=1
#     i+=1
    
# string = "(1+(2*3)+((8)/4))+1"
# stack = []

# count = 0
# for x in string:
#     if (x.isdigit() or x in ['+','*','-','/']) and len(stack) > count:
#         count = len(stack)
#     elif x == ')':
#         stack.pop()
#     elif x == '(':
#         stack.append('(')
# print(count)
        


# array = [1,1,1]
# array = [1,-1,0]
# k = 1
# hashmap = {0:1}
# sums = 0 
# count = 0
# for x in array:
#     sums += x
#     if hashmap.get(sums - k, None) != None :
#         count += hashmap[sums - k]
    
#     if hashmap.get(sums, None) == None:
#         hashmap[sums] = 1
#     else:
#         hashmap[sums] += 1

# print(count)
    
# string = "a)b(c)d"
# string = "lee(t(c)o)de)"
# ignorant_array = []

# i = 0
# while i < len(string):
#     if len(ignorant_array) > 0 and string[i] == ')' and string[ignorant_array[-1]] == '(':
#         ignorant_array.pop()
#     elif string[i] == '(' or string[i] == ')':
#         ignorant_array.append(i)
#     i+=1

# i = 0
# j = 0
# new_str = ""
# while i < len(string):
#     if j < len(ignorant_array) and i == ignorant_array[j]:
#         j+=1
#     else:
#         new_str += string[i]
#     i+=1
# print(new_str)




# string = "lee(t(c)o)de)"
# opens, closes, flag = 0,0,0

# for x in string:
#     if x == "(":
#         opens += 1
#         flag += 1
#     elif x == ")" and flag > 0:
#         closes += 1
#         flag -= 1

# k = min(opens, closes)
# opens = k
# closes = k

# i = 0
# new_str = ""
# while i < len(string):
#     if string[i] == '(' and opens > 0:
#         opens -= 1
#         new_str += '('
#     elif string[i] == ')' and closes > opens:
#         closes -= 1
#         new_str += ')'
#     elif string[i] not in ('(',')'):
#         new_str += string[i]
#     i+=1 

# print(new_str)

# string = "xaxcd"
# k = 4

# new_str = [x for x in string]

# i = 0
# while k > 0:
#     temp_size = k
#     left = ord(string[i])
#     right = ord(string[i])
#     tots_left = 0
#     tots_right = 0
#     j = 0
#     while j <= temp_size:
#         temp_left = (ord(string[i]) - 97 - j) % 26 + 97
#         temp_right = (ord(string[i]) - 97 + j) % 26 + 97
        
#         if temp_left < left:
#             left = temp_left
#             tots_left = j

#         if temp_right < right:
#             right = temp_right
#             tots_right = j
#         j += 1
    
        
#     if left < right:
#         k -= tots_left
#         new_str[i] = chr(left)
#     elif right < left:
#         k -= tots_right
#         new_str[i] = chr(right)

#     i+=1
# print(''.join(new_str))

# array =[[1]]
# numrows = 5

# for _ in range(2, numrows+1):
#     i = -1
#     j = 0
#     temp_arr = []
#     while j <= len(array[-1]):
#         element_1 = array[-1][i] if i >=0 else 0
#         element_2 = array[-1][j] if j < len(array[-1]) else 0
#         temp_arr.append(element_1 + element_2)
#         i+=1
#         j+=1
#     array.append(temp_arr)
# print(array)

# Merge Intervals
# array = [[1,3],[2,6],[8,10],[15,18]]
# new_stack = [array[0]]

# for i in range(1, len(array)):
#     if array[i][0] >= new_stack[-1][0] and array[i][0] <= new_stack[-1][1]:
#         temp_stack = [min(new_stack[-1][0], array[i][0]), max(new_stack[-1][1], array[i][1])]
#         new_stack.pop()
#         new_stack.append(temp_stack)
#     else:
#         new_stack.append(array[i])
# print(new_stack)


# nums1 = [2,0]
# i = 1
# nums2 = [1]
# k = 1

# i = i - 1
# k = k - 1
# j = len(nums1) - 1

# while k > -1:
#     if nums2[k] >= nums1[i]:
#         nums1[j] = nums2[k]
#         k -= 1
#     elif nums2[k] < nums1[i] and (i > 0):
#         nums1[j] = nums1[i]
#         i -= 1
#     elif i == 0:
#         nums1[j] = nums1[i]
#         nums1[i] = nums2[k]
#         k -= 1
#     j -= 1
# print(nums1)

# def not_zero(N):
#     if N == 0:
#         return 0 

#     x = (N % 10) if N > 9 else N
#     z = N // 10
#     new_val = not_zero(z)
#     if new_val == 0:
#         new_val = x
#     else:
#         new_val = new_val * 10
#         if x == 0:
#             new_val += 5
#         else:
#             new_val += x
#     return new_val

# print(not_zero(960))


# Merge two sorted arrays without extra space
# nums1 = [1,2,3,0,0,0] 
# m = 3 
# nums2 = [1,1,1] 
# n = 3
# i = m - 1 
# k = n - 1
# j = m + n - 1

# while k > -1 and i > -1:
#     if nums2[k] > nums1[i]:
#         nums1[j] = nums2[k]
#         k -= 1
#     else:
#         nums1[j] = nums1[i]
#         i -= 1
#     j -= 1

# for i in range(k+1):
#     nums1[i] = nums2[i]

# print(nums1)


# def rem_hi(string, 
#            index, 
#            prev_h, 
#            without_ca, 
#            with_ca, 
#            count):
    
#     removed = False
#     if string[index] == 'h':
#         prev_h = True
    
#     elif prev_h:
#         if string[index] == 'i':
#             with_ca.pop() if len(with_ca) > 0 else None
#             [with_ca.append(x) for x in 'bye']
#             without_ca.pop() if len(with_ca) > 0 else None
#             count += 1
#             removed = True
#         else:
#             prev_h = False

#     if not removed:
#         without_ca.append(string[index])
#         with_ca.append(string[index])
    
#     if index == len(string) - 1:
#         print(count)
#         print(''.join(without_ca))
#         print(''.join(with_ca))
#         return

#     rem_hi(string, index+1, prev_h,
#             without_ca, with_ca, count)

# rem_hi("abchihi", 0, False, [],[],0)


# def funcs(string, index):
#     if index == 0:
#         return ord(string[0]) - 48
    
#     new_element = funcs(string, index - 1)

#     new_element *= 10
#     new_element += ord(string[index]) - 48  

#     return new_element

# print(funcs('1234', 3))


# count = 0
# def mat(curr_row, curr_col, dest_row, dest_col, path):
#     if curr_col == dest_col and curr_row == dest_row:
#         print(path, end=" ")
#         return 1
#     elif curr_col > dest_col or curr_row > dest_row:
#         return 0 

#     count_1 = mat(curr_row+1, curr_col, dest_row, dest_col,path+"V")
#     count_2 = mat(curr_row, curr_col+1, dest_row, dest_col,path+"H")
#     count_3 = mat(curr_row+1, curr_col+1, dest_row, dest_col,path+"D")

#     return count_1 + count_2 + count_3

# print(mat(0, 0, 2, 2, ""))
# print(f"\n{count}")



            
# def permu(array:list):
#     i = len(array) - 1
#     while array[i-1] > array[i]:
#         i-=1
#     p = 0
#     if i > 0:
#         p = i-1

#     temp_i = i
#     mins = i
#     while temp_i < len(array):
#         if array[temp_i] < array[mins] and array[temp_i] > array[p]:
#             mins = temp_i
#         temp_i += 1

#     array[p], array[mins] = array[mins], array[p]
     
#     temp_arr = array[i:len(array)]
#     temp_arr.sort()
#     temp_arr = array[0:i] + temp_arr
    
#     array = temp_arr

# array = ['a','b','c']
# new_arr = array.copy()

# new_perms = []

# permu(new_arr)

# while ''.join(new_arr) > ''.join(array):
#     new_perms.append(new_arr.copy())
#     array = new_arr.copy()
#     permu(new_arr)


# for x in new_perms:
# 	print(''.join(x))

# def recurs(board ,dice, path):
#     if board == 0:
#         print(path, end=" ")
#         return 1
#     elif board < 0:
#         return 0
#     count = 0
#     for i in range(1,dice+1):
#         count += recurs(board-i, dice, path + f"{i}") 
    
#     return count


# board = 3
# dice = 3

# count = recurs(board, dice, "")
# print()
# print(count)


# def vivek_recurs(array, low, high, total):
#     sums = 0
#     count = 0
#     for i in range(low, high+1):
#         sums += array[i]
#         total -= array[i]
#         print(low, high,count)
#         if sums == total:
#             count += 1
#             count1, count2 = 0,0
#             count1 = vivek_recurs(array, low+1, i, sums)
#             if count1 == 0:
#                 count2 = vivek_recurs(array, i+1, high, sums)
#             count += count1 + count2
#     return count

# print(vivek_recurs([4,1,0,1,1,0,1],0,6, 8)
#      )       
# print(vivek_recurs([3,3,3],0,2, 9)
#  )       

# def binary_string(string, index, path):
#     if index == len(string):
#         print(path, end=" ")
#         return
    
#     if string[index] == "?":
#         binary_string(string, index+1, path+'0')
#         binary_string(string, index+1, path+'1')
#     else:
#         binary_string(string, index+1, path+string[index])


# string = "1??0?101"
# binary_string(string, 0, "")


# def last_index(array, found_index, index, to_find):
#     if index == len(array):
#         print(found_index)
#         return
    
#     if array[index] == to_find:
#         found_index = index
    
#     last_index(array, found_index, index+1, to_find)


# array = [3, 2, 1, 2, 3]
# to_find = 2
# last_index(array, -1, 0, to_find)


# Incomplete Rat Chase question, We need a approach and we need to think.
# def rat_chase(cur_row, cur_col, dest_row, dest_col, path, mat):
#     if cur_col > dest_col or cur_row > dest_row or mat[cur_row][cur_col] == 'X' or mat[cur_row][cur_col] == 'R':
#         return
#     elif cur_col == dest_col and cur_row == dest_row:
#         print(path)
#         return
    
#     rat_chase(cur_row + 1, cur_col ,dest_row ,dest_col, path+f"{cur_row},{cur_col} ", mat)
#     rat_chase(cur_row, cur_col + 1 ,dest_row ,dest_col, path+f"{cur_row},{cur_col} ", mat)
#     rat_chase(cur_row - 1, cur_col ,dest_row ,dest_col, path+f"{cur_row},{cur_col} ", mat)
#     rat_chase(cur_row, cur_col - 1 ,dest_row ,dest_col, path+f"{cur_row},{cur_col} ", mat)
    




# rows = 5 
# cols = 4

# mat = [ 
#     ['O', 'X', 'O', 'O'],
#     ['O', 'O', 'O', 'X'],
#     ['O', 'X', 'O', 'X'],
#     ['X', 'O', 'O', 'X'],
#     ['X', 'X', 'O', 'O'],
# ]
# rat_chase(0 , 0, rows - 1, cols - 1, "", mat)


# def triangle(n):
#     if n == 1:
#         return 1
    
#     below = triangle(n-1)

#     return below + n

# print(triangle(int(input())))


# Binary search find left and right index
# def left_binary_search(array, low, high, target):
#     while low <= high:
#         mid = (low + high) // 2
#         if array[mid] == target:
#             if (mid > 0 and array[mid - 1] != target) or mid == 0:
#                 return mid
#             else:
#                 high = mid - 1
#         elif array[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1

# def right_binary_search(array, low, high, target):
#     while low <= high:
#         mid = (low + high) // 2
#         if array[mid] == target:
#             if (mid < len(array)-1 and array[mid + 1] != target) or mid == len(array)-1:
#                 return mid
#             else:
#                 low = mid + 1
#         elif array[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1

# nums = [2,2]
# target = 2
# print([left_binary_search(nums, 0, len(nums)-1, target), right_binary_search(nums, 0, len(nums)-1, target)])


 
# nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
# target = 2
# print(binsearch(nums, 0, len(nums)- 1, target))       
                
# def minimum_binary_search(array, low, high):
#     mins = array[low]

#     while low <= high:
#         mid = (low + high) // 2

#         if array[mid] < mins:
#             mins = array[mid]
#         elif array[mid] >= array[low]: # left sorted
#             if array[low] < array[high]:
#                 high = mid - 1
#             else:
#                 low = mid + 1
#         else: # right sorted
#             high = mid - 1
#     return mins



# print(minimum_binary_search(nums,0,len(nums)-1))






