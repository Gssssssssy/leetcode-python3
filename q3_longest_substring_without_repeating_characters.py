class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans, start = 0, 0
        indexes = {}
        for end, cur in enumerate(s):
            if cur in indexes and indexes.get(cur, 0) >= start:
                start = indexes.get(cur, 0) + 1

            indexes[cur] = end
            ans = max(ans, end - start + 1)
        return ans
