class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == '+' or tokens[i] == '-' or tokens[i] == '*' or tokens[i] == '/':
                n1 = stack.pop()
                n2 = stack.pop()
                if tokens[i] == '+':
                    val = eval(str(n1 + n2))
                if tokens[i] == '-':
                    val = eval(str(n2 - n1))
                if tokens[i] == '*':
                    val = eval(str(n1 * n2))
                if tokens[i] == '/':
                    val = eval(str( n2/n1))
                stack.append(int(val))
            else:
                stack.append(int(tokens[i]))
        return stack[0]
        

        