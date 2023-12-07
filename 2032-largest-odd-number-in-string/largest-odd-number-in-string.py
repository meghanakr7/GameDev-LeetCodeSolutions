class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1, -1, -1):
            print('num i is ',num[i])
            if int(num[i]) % 2:
                print('its odd ',num[i])
                return num[0:i+1]
        return ""