class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        def canPlaceBalls(d):
            count = 1  
            last_position = position[0]
            
            for i in range(1, len(position)):
                if position[i] - last_position >= d:
                    count += 1
                    last_position = position[i]
                    if count == m:
                        return True
            return False
        
        
        print("Type of position:", type(position))
        print("Content of position:", position)
        
        
        if not isinstance(position, list):
            raise TypeError("position must be a list")
        if not all(isinstance(x, int) for x in position):
            raise TypeError("All elements in position must be integers")
        
        
        print("Before sorting:", position)
        
        
        position.sort()
        
        
        print("After sorting:", position)
        
        
        left, right = 1, position[-1] - position[0]
        while left < right:
            mid = (left + right + 1) // 2
            if canPlaceBalls(mid):
                left = mid
            else:
                right = mid - 1
        
        return left
