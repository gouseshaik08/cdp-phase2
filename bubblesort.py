def bubblesort(nums):
    n = len(nums)
    pos = n-1
    while pos > 0:
        for index in range(0,pos):
            if nums[index] > nums[index+1]:
                nums[index],nums[index+1] = nums[index+1],nums[index]
        pos-=1
nums = [66,56,3,9,5,-65,42,63,2,0,36,59,6]
print("Before Sorting :",nums)
bubblesort(nums)
print("After Sorting :",nums)