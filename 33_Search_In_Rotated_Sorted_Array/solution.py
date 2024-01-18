class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # loop through array and try to find pivot index (index where array is rotated)
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # we found k (pivot index)
                if target < nums[0]:
                    return self.bin_search(nums, i + 1, len(nums) - 1, target)
                elif target > nums[len(nums) - 1]:
                    return self.bin_search(nums, 0, i, target)
                else:
                    return -1
        
        # if index of rotation wasn't found, array is already sorted
        return self.bin_search(nums, 0, len(nums) - 1, target)


    def bin_search(self, arr, low, high, target):
        """
        :type arr: List[int]
        :type low: int
        :type high: int
        :type target: int
        :rtype: int
        """

        if low <= high:
            p = (high + low) // 2
            
            if arr[p] == target:
                return p
            elif arr[p] < target:
                return self.bin_search(arr, p + 1, high, target)
            else:
                return self.bin_search(arr, low, p - 1, target)
        
        else:
            return -1
