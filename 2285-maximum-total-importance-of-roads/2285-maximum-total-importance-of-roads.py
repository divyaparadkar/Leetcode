class Solution(object):
    def maximumImportance(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
    
        degree = [0] * n
        for u, v in edges:
            degree[u] += 1
            degree[v] += 1
        
    
        node_importance = sorted(range(n), key=lambda x: degree[x], reverse=True)
        

        importance = [0] * n
        for i, node in enumerate(node_importance):
            importance[node] = n - i
        
        total_importance = 0
        for u, v in edges:
            total_importance += importance[u] + importance[v]
        
        return total_importance
