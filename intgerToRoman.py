class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = [["","I","II","III","IV","V","VI","VII","VIII","IX"],
                 ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"],
                 ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"],
                 ["","M","MM","MMM"]]
        count = 0
        ans = ''
        while(num!=0):
            a = num%10
            num = num/10
            s = roman[count][a]
            ans = s+ans
            count+=1
        return ans

solution = Solution()
print solution.intToRoman(3333)

