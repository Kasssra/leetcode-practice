class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_index = len(nums) - 1
        max_reach = 0
        for i in range(last_index):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= last_index:
                return True
        return max_reach >= last_index
    

    
    
        
        
    