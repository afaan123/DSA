class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s)!=len(t)):
            return False
        return sorted(s)==sorted(t)

#Time Complexity: O(nlogn+ mlogm)
#Space Complexity: O(1) or O(n+m)

