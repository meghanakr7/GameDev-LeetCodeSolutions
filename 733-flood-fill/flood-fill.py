class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        print("m and n are ",m,n)
        s = set()
        def bfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or image[i][j] != oldColor or (i,j) in s:
                print("i came here")
                return 
            if (i,j) not in s:
                s.add((i,j))
            if image[i][j] == oldColor:
                image[i][j] = color
            return bfs(i-1, j) or bfs(i, j-1) or bfs(i, j+1) or bfs(i+1,j)
        oldColor = image[sr][sc]
        bfs(sr, sc)
        print("Grid now is ",image)
        return image