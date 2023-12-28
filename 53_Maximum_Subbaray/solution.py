class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Create array to save sum
        res = [0] * len(nums)
        res[0] = nums[0]
        
        # Loop through array and check if current element is bigger that last sum
        for n in range(1, len(nums)):
            if nums[n] > res[n - 1] and res[n - 1] < 0:
                # If current number is bigger then last sum, save that number
                res[n] = nums[n]
            else:
                # In other case, add that number to previous sum
                res[n] = res[n - 1] + nums[n]
            
        # Return result
        return max(res)