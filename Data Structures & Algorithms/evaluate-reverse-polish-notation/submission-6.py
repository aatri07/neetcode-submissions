class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        stack = []
        for i in tokens:
            if i in "+*/-":
                operand_b = stack.pop()
                operand_a = stack.pop()
                if i == "+":
                    res = int(operand_a) + int(operand_b)
                elif i == "-":
                    res = int(operand_a) - int(operand_b)
                elif i == "*":
                    res = int(operand_a) * int(operand_b)
                elif i == "/":
                    res = int(operand_a / operand_b)
                stack.append(res)
            else:
                stack.append(int(i))
        
        return stack[0]