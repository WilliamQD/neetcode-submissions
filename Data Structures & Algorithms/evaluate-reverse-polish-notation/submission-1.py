class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for tok in tokens:
            if tok in operators:
                num2 = int(stack.pop())
                num1 = int(stack.pop())

                if tok == '+':
                    stack.append(num1+num2)
                elif tok == '-':
                    stack.append(num1-num2)
                elif tok == '*':
                    stack.append(num1*num2)
                else:
                    stack.append(int(num1 / num2))
            else:
                stack.append(tok)

        return int(stack[0])