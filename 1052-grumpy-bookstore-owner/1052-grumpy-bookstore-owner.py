class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        total_satisfied = 0
        extra_satisfied = 0
        max_extra_satisfied = 0
        
    
        for i in range(len(customers)):
            if grumpy[i] == 0:
                total_satisfied += customers[i]
        
        
        for i in range(minutes):
            if grumpy[i] == 1:
                extra_satisfied += customers[i]
        
        max_extra_satisfied = extra_satisfied
        
        
        for i in range(minutes, len(customers)):
            if grumpy[i] == 1:
                extra_satisfied += customers[i]
            if grumpy[i - minutes] == 1:
                extra_satisfied -= customers[i - minutes]
            
            max_extra_satisfied = max(max_extra_satisfied, extra_satisfied)
        
        return total_satisfied + max_extra_satisfied
