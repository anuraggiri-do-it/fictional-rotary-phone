def removeDuplicates( nums):
        if len(nums) == 0:
            return 0

        write = 1  

        for read in range(1, len(nums)):
            if nums[read] != nums[read - 1]:
                nums[write] = nums[read]
                write += 1

        return write
nums = [-1,-1,1,1,2,3,3,3,3,4,5,5,6,6,6,8,8]
k = removeDuplicates(nums)

print("Count:", k)
print("Unique elements:", nums[:k])