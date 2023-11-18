class Solution:
    def customSortString(self, order: str, s: str) -> str:
        newStr = []*len(s)
        orderStrIndexes = []
        for i in range(len(s)):
            if s[i] in order:
                orderStrIndexes.append(i)
            else:
                newStr.insert(i, s[i])
        # print("newStr till now ",newStr)
        for i in range(len(order)):
            if order[i] in s:
                count = s.count(order[i])
                while count:
                    newStr.insert(orderStrIndexes[0], order[i])
                    orderStrIndexes = orderStrIndexes[1 : len(orderStrIndexes)]
                    count -= 1
        # print("Now newStr is ",newStr)
        return "".join(newStr)
            