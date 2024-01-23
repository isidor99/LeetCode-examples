class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # create one more array to store previous sums
        arr = [0] * len(nums)
        
        # loop through array of numbers
        for i in range(len(nums)):
            if i == 0 or i == 1:
                # for the first two numbers, only save them
                arr[i] = nums[i]
            elif i == 2:
                # for third number only add first saved number and save their sum
                arr[i] = nums[i] + arr[0]
            else:
                # for the rest of array
                arr[i] = max(nums[i] + arr[i - 2], nums[i] + arr[i - 3])
        
        # return maximum element from array
        return max(arr)
