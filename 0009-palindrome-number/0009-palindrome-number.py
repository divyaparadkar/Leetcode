class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num_str = str(x)
        return num_str == num_str[::-1]

solution = Solution()
number = 12321
if solution.isPalindrome(number):
    print("{} is a palindrome.".format(number))
else:
    print("{} is not a palindrome.".format(number))