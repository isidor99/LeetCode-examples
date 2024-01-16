class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        # join two arrays int one sorted array
        i = j = 0
        res = []
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i = i + 1
            else:
                res.append(nums2[j])
                j = j + 1
                
        res.extend(nums1[i:])
        res.extend(nums2[j:])
        
        # if number of elements in result array is even, then median is average of two middle elements
        # if number of elements in result array is odd, then median is middle element
        l = len(res)
        if l % 2 == 1:
            return res[l // 2]
        else:
            return (res[l // 2] + res[l // 2 - 1]) / 2.0
