class Solution(object):
    def longestSubarray(self, nums, limit):
        max_d = deque()
        min_d = deque()
        left = 0
        res = 0
       

        for right in range(len(nums)):
            
            while max_d and nums[max_d[-1]] <= nums[right]:
                max_d.pop()
            max_d.append(right)

        
            while min_d and nums[min_d[-1]] >= nums[right]:
                min_d.pop()
            min_d.append(right)

            
            while nums[max_d[0]] - nums[min_d[0]] > limit:
                left += 1
                if max_d[0] < left:
                    max_d.popleft()
                if min_d[0] < left:
                    min_d.popleft()

            res = max(res, right - left + 1)
        
        return res
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        