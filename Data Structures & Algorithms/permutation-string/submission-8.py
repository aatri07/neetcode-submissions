class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1)
        s1freq = self.freqMap(s1)
        while (right <= len(s2)):
            subs2 = s2[left:right]
            if (s1freq == self.freqMap(subs2)):
                return True
            right += 1
            left += 1
        return False

    

    def freqMap(self, s1: str) -> list[int]:
        res = [0] * 26
        for char in s1:
            res[ord(char) - ord('a')] += 1
        return res

        