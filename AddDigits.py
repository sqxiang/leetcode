import re
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        result = 0 if num == 0 else 9 if num % 9 == 0 else num % 9
        return result


solution = Solution()
print solution.addDigits(8)