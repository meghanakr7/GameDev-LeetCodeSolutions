class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # print('val is ', int(math.log(n,2)),math.log(n,2), abs(int(math.log(n,2)) - math.log(n,2)) )
        # print('val is ', math.pow(10, -6))
        if(n == 0):
            return False

        if( n > 0 and abs(int(math.log(n,2)) - math.log(n,2))<=math.pow(10, -9)):
            return True
        return False
        