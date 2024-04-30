def kadanes(nums):
    maxSum = nums[0]
    curSum = 0

    for n in nums:
        curSum = max(curSum += n, 0)
        maxSum = max(maxSum, curSum)

    return maxSum