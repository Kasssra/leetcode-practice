# Example 1:

# Input: 
nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

# I can use the algorithm below to swap the element on an array in place

left, right = 0, len(nums)-1
while left < right:
    nums[left], nums[right] = nums[right], nums[left]
    left+=1
    right=-1


# in cpp and java:   
# int temp = nums[left];
# nums[left] = nums[right];
# nums[right] = temp;

left, right = 0, k-1
while left < right:
    nums[left], nums[right] = nums[right], nums[left]
    left+=1
    right-=1

left, right = k, len(nums)-1
while left < right:
    nums[left], nums[right] = nums[right], nums[left]
    left+=1
    right-=1 