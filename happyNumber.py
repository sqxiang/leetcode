class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n==1):
            return True

        p = list()
        while(True):
            m=0
            p.append(n)
            while(n>0):
                m =m+(n%10)**2
                n=n/10
            n = m
            if(n==1):
                return True
            if(n in p):
                return False

solution = Solution()
print solution.isHappy(11)