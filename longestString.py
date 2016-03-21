import string
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        p,l= list(),list()
        for i in range(len(s)):
            if(s[i] in p):
                l.append(len(p))
                a = p.index(s[i])
                p = p[a+1:]
            p.append(s[i])
        l.append(len(p))
        result = max(l)
        return result

solution = Solution()
print solution.lengthOfLongestSubstring('')
