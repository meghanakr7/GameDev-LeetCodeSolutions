class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] == '*':
                # print("Befor stack is ",stack)
                stack.pop()
                # print("After that stack is ",stack)
            else:
                stack.append(s[i])
        # print("stack is ",stack)
        # print("str is ", "".join(stack))
        res = "".join(stack)
        return res


        