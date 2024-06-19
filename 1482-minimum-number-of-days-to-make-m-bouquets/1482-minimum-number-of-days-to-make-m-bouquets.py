class Solution(object):
    def minDays(self, bloomDay, m, k):
        def canMakeBouquets(day):
            bouquets = 0
            flowers = 0
            for bloom in bloomDay:
                if bloom <= day:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
                if bouquets >= m:
                    return True
            return False

        # Check if it's impossible to create m bouquets
        if m * k > len(bloomDay):
            return -1

        # Binary search for the minimum number of days
        left, right = 1, max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            if canMakeBouquets(mid):
                right = mid
            else:
                left = mid + 1

        return left
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
       