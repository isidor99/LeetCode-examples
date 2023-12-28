class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Space and time complexity is O(n)
        # Create array to save sum
        res = [*nums]
        
        # Loop through array and save bigger number between current number and sum of current number and last one
        for n in range(1, len(nums)):
            res[n] = max(nums[n], nums[n] + res[n - 1])
            
        # Return result
        return max(res)