class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        leftstack = []
        leftChars = set()
        leftChars.add("[")
        leftChars.add("(")
        leftChars.add("{")
        

        for i in s:
            if i in leftChars:
                leftstack.append(i)
            else:
                if not leftstack:
                    return False
                thisChar = leftstack.pop()
                if thisChar == "(" and i != ")":
                    return False
                elif thisChar == "[" and i != "]":
                    return False
                elif thisChar == "{" and i != "}":
                    return False
        
        return(not leftstack)

        