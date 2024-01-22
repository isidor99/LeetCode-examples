class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        # sort array
        intervals = sorted(intervals, key=lambda x: x[0])
        
        # add first element of sorted array to result array
        result_arr = [intervals[0]]
        
        # loop starting from second element
        for i in range(1, len(intervals)):
            
            # get length of result array
            l = len(result_arr)
            
            # if end of interval, in last interval in result array, is less than start of interval
            # then we have overlapping intervals
            # else add new interval to result array
            if result_arr[l - 1][1] >= intervals[i][0]:
                result_arr[l - 1][1] = max(result_arr[l - 1][1], intervals[i][1])
            else:
                result_arr.append(intervals[i])
        
        # return result
        return result_arr
