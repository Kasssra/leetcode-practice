nums = [1,1,1,2,3,3,4,5,6,7,7,8,9]
cnt = 1
p1 = 1
for p2 in range(len(nums)):
    if nums[p1] == nums[p2]:
        nums[p1] = nums[p2]
    if p1 != p2:
        p1 =+1