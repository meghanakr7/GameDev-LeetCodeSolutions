class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        length = len(str(low))
        print('len is ',length)
        start_num = int(str(low)[0])
        print('start num is ',start_num)
        num = "0"
        res = []
        if(length > 10 - start_num):
            length += 1
            start_num = 1
        while num and (int(num) < high):
            cur = 0
            init_s = start_num
           
            num = ""
            while cur < length:
                num += str(start_num)
                cur += 1
                start_num += 1
            start_num = init_s
            if num and (int(num) <= high) and (int(num) >= low):
                res.append(int(num))
            
            if(length > 9 - start_num):
                length += 1
                start_num = 1
            else:
                start_num += 1
            print('at the end ', int(num))
        print('res is ',res)
        return res
        


            

        