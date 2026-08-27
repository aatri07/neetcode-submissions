class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        arr_1 = [0] * 26
        arr_2 = [0] * 26
        for char in s:
            arr_1[ord(char) - ord("a")] += 1
        
        for char in t:
            arr_2[ord(char) -  ord("a")] += 1

        for i in range(26):
            if arr_1[i] != arr_2[i]:
                return False
        
        return True



        