def small(nums, left = None, right = None):

    if left is None and right is None:
        left,right = 0,len(nums)-1

    if left > right:
        return left + nums[0]
    mid = left + (right-left) // 2

    if nums[mid] == nums[0]+mid:
        return small(nums, mid+1,right)
    else:
        return small(nums, left,mid-1)
    
nums = [1,2,4,5,6,7,8,9]
print(small(nums))
    