class Solution(object):
    def findCenter(self, edges):
         
        u1, v1 = edges[0]
        u2, v2 = edges[1]
        
        
        if u1 == u2 or u1 == v2:
            return u1

        return v1
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        