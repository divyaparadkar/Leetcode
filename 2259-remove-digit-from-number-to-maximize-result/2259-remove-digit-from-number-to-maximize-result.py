
class Solution(object):
    def removeDigit(self, number, digit):
        """
        :type number: str
        :type digit: str
        :rtype: str
        """
        max_number = ''
        
        for i in range(len(number)):
            if number[i] == digit:
                # Create a new number by removing the i-th digit
                new_number = number[:i] + number[i+1:]
                # Update max_number if the new number is larger
                if new_number > max_number:
                    max_number = new_number
        
        return max_number        