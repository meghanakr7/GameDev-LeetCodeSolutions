class Solution:
    def countHomogenous(self, s: str) -> int:
        h = set()
        d = defaultdict(int)
        allchars = list(set(s))
        count = 0
        print("All chars are ",allchars)
        prev = s[0]
        i = 0
        finalcount = 0
        while i < len(s):
            prev = s[i]
            if prev == s[i]:
                count = 0
                while i < len(s) and prev == s[i]:
                    
                    prev = s[i]
                    i += 1
                    count += 1
                finalcount += (count * (count + 1) //2)
            print("After coming out while is ",count,prev)
        print("Final c is ",finalcount)
        return finalcount % (10**9 + 7)


            # char = allchars[i]
            # charCount = s.count(allchars[i])
            # print("Chars chount is ", char, charCount)
            # count += (charCount) * (charCount + 1) // 2
            # print("Count is ",count)
        


