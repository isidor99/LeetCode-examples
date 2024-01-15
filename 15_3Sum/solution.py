class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Create result array
        res = []
        
        # Sort array
        nums.sort()
        
        # Loop
        for i in range(0, len(nums) - 2):
            # Get rid off duplicates with this condition
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Create "two pointers"
            j = i + 1
            k = len(nums) - 1
            target = -nums[i]

            # Loop while j is less than k            
            while j < k:
                # Sum of element at j and k positions
                sum = nums[j] + nums[k]
                
                # Is sum is equal to target, triple was found
                if sum == target:
                    res.append([nums[i], nums[j], nums[k]])
                    
                    # Skip same numbers
                    while j < k and nums[j] == nums[j + 1]:
                        j = j + 1
                    
                    while j < k and nums[k] == nums[k - 1]:
                        k = k - 1
                        
                    # Finally, increment/decrement "pointers"
                    j = j + 1
                    k = k - 1
                
                elif sum < target:
                    # If sum is less that target, increment j, else decrement k
                    j = j + 1
                else:
                    k = k - 1
                        
        return res
