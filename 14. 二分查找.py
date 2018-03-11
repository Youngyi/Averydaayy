# class Solution:
#     # @param nums: The integer array
#     # @param target: Target number to find
#     # @return the first position of target in nums, position start from 0
#     def binarySearch(self, nums, target):
#         # write your code here
#         begin, end = 0, len(nums)
#         while begin <= end:
#             mid = (begin + end) / 2
#             if nums[mid] > target:
#                 end = mid -1
#             elif nums[mid] < target:
#                 begin = mid +1
#             else:
#                 for i in xrange(mid-1,-1,-1):
#                     if nums[i] != target:
#                         return i+1
#                 return 0
#         return -1
class Solution:
    def fun(self, nums, target):
        start, end = 0, len(nums)-1
        while start+1 <= end:
            mid = (start+end)/2
            if nums[mid] > target:
                end = mid -1
            elif nums[mid] < target:
                start = mid +1
            else:
                for i in range(mid-1, -1, -1):
                    if nums[i] != target:
                        return i+1
                return  0
        return -1
#     everyda coming "yyangcp"
