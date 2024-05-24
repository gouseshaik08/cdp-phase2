def selectionsort(nums):
    n = len(nums)
    pos = n-1
    while pos>0:
        maxeleindex =  pos
        for index in range(0,pos+1):
            if nums[index] > nums[maxeleindex]:
                maxeleindex = index
        if maxeleindex!=index:
            nums[maxeleindex],nums[pos] = nums[pos],nums[maxeleindex]
        pos-=1
nums = [66,56,3,9,5,-65,42,63,2,0,36,59,6]
print("Before Sorting :",nums)
selectionsort(nums)
print("After Sorting :",nums)