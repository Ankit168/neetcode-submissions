class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+','-','*','/'}
        result = []
        for token in tokens:
            if token in operators:
                second_value = result.pop()
                first_value = result.pop()
                if token == '+':
                    temp = first_value+second_value
                elif token == '-':
                    temp = first_value-second_value
                elif token == '*':
                    temp = first_value*second_value
                elif token == '/':
                    temp = temp = int(first_value/second_value)
                result.append(temp)
            else:
                result.append(int(token))

        return result[-1]


