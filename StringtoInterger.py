class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        p=0
        sgn = 1
        result = 0
        minint,minmax = -1<<31,(1<<31)-1
        if len(str)==0:
            return 0
        while(str[p] == ' '):
            p+=1
        if str[p] == '+' or str[p] == '-':
            if str[p] == '-':
                sgn = -1
            p+=1
        while(p<len(str) and str[p]>='0' and str[p]<='9'):
            result = result*10 + int(str[p])
            p+=1
        result = sgn*result
        if(result>minmax):return minmax
        if result<minint:return minint

        return result

solution = Solution()
print solution.myAtoi('     -19999999999999999999999999999eeee')

