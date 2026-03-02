def sortedSquares(nums):
    n = len(nums)
    result = [0] * n
    
    left = 0
    right = n - 1
    
    # Fill result from right to left
    for i in range(n - 1, -1, -1):
        
        # Compare absolute values
        if abs(nums[left]) > abs(nums[right]):
            result[i] = nums[left] * nums[left]
            left += 1
        else:
            result[i] = nums[right] * nums[right]
            right -= 1
    
    return result