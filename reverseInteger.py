class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = int(str(x)[::-1]) if x>=0 else -int(str(abs(x))[::-1])
        if(x>2**32-1 or x<-2**32-1 or s>2**32-1 or s<-2**32-1):
            return 0
        return s


solution = Solution()
print solution.reverse(2147483651)
print 2**31-1
