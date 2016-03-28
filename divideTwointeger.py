class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MIN_INT,MAX_INT = -1<<31,(1<<31)-1
        print MAX_INT
        flag = 0
        ans = 0
        if dividend<0:
            flag,dividend = flag^1,-dividend
        if divisor<0:
            flag,divisor = flag^1,-divisor
        while dividend>=divisor:
            count,newDivisor = 1,divisor
            while newDivisor+newDivisor<=dividend:
                newDivisor = newDivisor+newDivisor
                count = count + count
            dividend-=newDivisor
            ans += count
        if ans>MAX_INT:
            return MAX_INT
        return ans if flag==0 else -ans

solution = Solution()
print solution.divide(-2147483648,-1)