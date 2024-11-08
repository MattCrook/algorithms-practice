#------------------------------------------------#
#------------------------------------------------#

class Solution:
    def reverseString(self, s):
        for i in range(len(s)//2):
            s[i], s[~i] = s[~i], s[i]

s = Solution()
print(s.reverseString("cat"))
