class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
      # Dictionary to hold mappings of open and close brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        # Initialize an empty stack
        stack = []

        # Iterate through each character in the string
        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Pop the topmost element from the stack if it is not empty; otherwise assign a dummy value '#'
                top_element = stack.pop() if stack else '#'
                # Check if the popped element is the corresponding opening bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it is an opening bracket, push it onto the stack
                stack.append(char)

        # If the stack is empty, all opening brackets had corresponding closing brackets in the correct order
        return not stack

# Example usage:
sol = Solution()
print(sol.isValid("()"))     # Output: True
print(sol.isValid("()[]{}")) # Output: True
print(sol.isValid("(]"))     # Output: False
print(sol.isValid("([)]"))   # Output: False
print(sol.isValid("{[]}"))   # Output: True