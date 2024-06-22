class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = {0: 1}
        odd = 0
        result = 0

        for num in nums:
            if num % 2 == 1:
                odd += 1
            
            if (odd - k) in count:
                result += count[odd - k]

            if odd in count:
                count[odd] += 1
            else:
                count[odd] = 1
        
        return result