class Solution(object):
    def minKBitFlips(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        flip = [0] * n
        flipped = 0
        result = 0

        for i in range(n):
            if i >= k:
                flipped ^= flip[i - k]
            if nums[i] == flipped:
                if i + k > n:
                    return -1
                result += 1
                flipped ^= 1
                flip[i] = 1

        return result
        