class Solution(object):
    def getAncestors(self, n, edges):
        from collections import defaultdict, deque

        
        graph = defaultdict(list)
        for u, v in edges:
            graph[v].append(u)

    
        ancestors = [set() for _ in range(n)]

        
        def bfs(start):
            queue = deque([start])
            visited = set([start])
            while queue:
                node = queue.popleft()
                for ancestor in graph[node]:
                    if ancestor not in visited:
                        visited.add(ancestor)
                        queue.append(ancestor)
                        ancestors[start].add(ancestor)
                        ancestors[start].update(ancestors[ancestor])

        
        for i in range(n):
            bfs(i)

        #
        return [sorted(list(ancestor_set)) for ancestor_set in ancestors]

        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        