class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if (op == "C"):
                stack.pop()
            elif (op == "D"):
                prev = stack[len(stack) - 1]
                stack.append(prev * 2)
            elif (op == "+"):
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op2)
                stack.append(op1)
                stack.append(int(op1) + int(op2))
            else:
                stack.append(int(op))
        sum = 0
        for a in stack:
            sum += a
        
        return sum