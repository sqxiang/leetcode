class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dct = {'(':')','{':'}','[':']',')':'','}':'',']':''}
        top_index = -1
        stack = []
        for i in range(len(s)):
            top_index+=1
            stack.append(s[i])
            if(top_index>=1 and stack[top_index]==dct[stack[top_index-1]]):
                top_index-=2
                stack.pop()
                stack.pop()
        if stack == []:
            return True
        return False

solution = Solution()
print solution.isValid('[')
