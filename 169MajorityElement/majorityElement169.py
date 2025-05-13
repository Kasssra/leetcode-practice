# using Boyer-Moore Voting Algorithm

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)) :
            currentNum = nums[i]
            if count == 0:
                candidate = currentNum
            if candidate == currentNum:
                count+=1
            else:
                count-=1
        return candidate
    

# solution with better time complexity:
class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums) // 2]


# solution with better space complexity:

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         for i in nums:
#             k=0
#             h=0
#             for j in range(len(nums)-1+h,-1,-1):
#                 if i==nums[j]:
#                     k=k+1
#                     nums.pop(j)
#                     h=h+1
#                 if k > (len(nums)+h)/2:
#                     return i

    


    