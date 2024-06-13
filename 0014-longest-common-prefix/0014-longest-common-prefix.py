class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
    
        prefix = strs[0]
        
        
        for string in strs[1:]:
        
            while string[:len(prefix)] != prefix:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix

solution = Solution()
strs = ["flower", "flow", "flight"]
print(solution.longestCommonPrefix(strs)) 