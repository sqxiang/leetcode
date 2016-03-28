import re
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = re.match(p,s)
        if(m):
            if(m.end()==len(s)):
                return True
        return False

soulution = Solution()
print soulution.isMatch("sss",'.*')