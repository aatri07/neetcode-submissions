class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqMap = {}
        res = []
        index = 0
        for i in range(len(strs)):
            freqs = [0] * 26
            for j in range(len(strs[i])):
                freqs[ord(strs[i][j]) - ord("a")] += 1
            
            freq_tuple = tuple(freqs)
            if freq_tuple in freqMap:
                res[freqMap[freq_tuple]].append(strs[i])
            else:
                freqMap[freq_tuple] = index
                res.append([strs[i]])  
                index += 1

        return res
        
        
        