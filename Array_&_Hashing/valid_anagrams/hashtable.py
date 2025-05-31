class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')]=count[ord(s[i]) - ord('a')]-1
            count[ord(t[i]) - ord('a')]=count[ord(t[i]) - ord('a')]+1

        for val in count:
            if val != 0:
                return False
        return True 

#Time Complexity: O(n+m)
#Space Complexity: O(1)