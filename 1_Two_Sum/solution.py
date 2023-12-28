class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # O(n)
        hash_map = {}
        for i in range(len(nums)):
            key = nums[i]
            value = target - nums[i]
            
            # Check if hash map contains key equals to value
            if value in hash_map:
                return [hash_map[value], i]

            # Save index in hash map
            hash_map[key] = i

        return None
