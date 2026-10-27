class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqMap = {}
        left = 0
        right = 0
        while (right < len(s)):
            if (s[right] in freqMap):
                freqMap[s[right]] += 1
            else:
                freqMap[s[right]] = 1
            size = right - left + 1
            mostChar = self.findMaxFrequency(freqMap)
            if (k < size - freqMap[mostChar]):
                freqMap[s[left]] -= 1
                left += 1
            right += 1
        size = right - left
        return size

    def findMaxFrequency(self, freqMap: dict) -> str:
        max = 0
        res = ''
        for char in freqMap:
            if (freqMap[char] > max):
                max = freqMap[char]
                res = char
        return res





        