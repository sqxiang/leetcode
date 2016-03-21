class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        line = dict()
        i = 0
        result=''
        for k in range(numRows):
            line[k]=''
        step = 1
        if(numRows==1):
            return s
        for c in s:
            line[i]+=c
            i+=step
            if(i==numRows-1):
                step=-1
            if(i==0):
                step=1
        for i in line:
            result = result+line[i]
        return result


solution = Solution()
print solution.convert('AB',1)