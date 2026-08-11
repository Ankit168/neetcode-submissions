class Solution:
    def calPoints(self, operations: List[str]) -> int:
        operation_stack = []

        for operation in operations:
            if operation == "D":
                temp = 2*operation_stack[-1]
                operation_stack.append(temp)
            elif operation == "C":
                temp = operation_stack.pop()
            elif operation == "+":
                temp = operation_stack[-1] + operation_stack[-2]
                operation_stack.append(temp)
            else:
                operation_stack.append(int(operation))
        
        return sum(operation_stack)