class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #nums = [1,1,1,2,3,3,4,5,6,7,7,8,9]
        p1 = 0
        p2 = 0
        cnt = 0
        while p1 < len(nums):
            if p1 == p2:
                cnt += 1
                p1 += 1
            elif p1 > p2:
                if nums[p1] == nums[p2]:
                    del(nums[p1])
                elif nums[p1] != nums[p2]:
                    p2 = p1
                    p1 += 1
                    cnt +=1
        k = cnt
        return k
        

#the better solution
#for p2 in range(1, len(nums)):
#    if nums[p2] != nums[p1 - 1]:  # Found a unique element
#        nums[p1] = nums[p2]
#        p1 += 1
#        cnt += 1  # Increment count of unique elements
        