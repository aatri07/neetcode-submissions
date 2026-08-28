class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_arr = []
        for str in strs:
            encoded_arr.append(str)
            encoded_arr.append("é")
        
        return "".join(encoded_arr)

    def decode(self, s: str) -> List[str]:
        decoded_arr = []
        new_string = []
        for char in s:
            if char != "é":
                new_string.append(char)
            else:
                decoded_arr.append("".join(new_string))
                new_string = []
        
        return decoded_arr

