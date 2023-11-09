class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        output = [pref[0]]
        prevXor = pref[0]
        for i in range(1, len(pref)):
            # print("len of i is ",i, pref[i])
            output.append(prevXor ^ pref[i])
            # print("Output of i is ",output)
            prevXor = prevXor ^ output[i]
        # print("Final is ",output)
        return output

        