class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # Create variables: start index, length of longest substring (res) and hash map (letter: last_index)
        start = 0
        res = 0
        hash_map = {}
        
        for i, letter in enumerate(s):
            # Get last index of current letter
            letter_index = hash_map.get(letter, -1)
            
            # If letter was before found in string, then increase start index by one
            if letter_index >= start:
                start = letter_index + 1
            
            # Calculate result
            res = max(res, i - start + 1)
            
            # Save last letter index in hash map
            hash_map[letter] = i

        # Return result
        return res
                