nums = [0,0,1,1,1,1,2,3,3,3,4,4,5,6,6,6,6,6,6]
p1 = 0
p2 = 1
while p2 < len(nums):
    if (nums[p1] == nums[p2] and ((p2-p1) == 1)):
        p2 += 1
    elif (nums[p1] == nums[p2] and ((p2-p1) >= 1)):
        p2 += 1 
    elif (nums[p1] != nums[p2]):
        p1 = p2
        p2 += 1
print(nums)
