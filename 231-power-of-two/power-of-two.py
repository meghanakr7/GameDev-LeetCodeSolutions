class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if(n == 0):
            return False
        if( n > 0 and abs(int(math.log(n,2)) - math.log(n,2))<=math.pow(10, -9)):
            return True
        return False
        