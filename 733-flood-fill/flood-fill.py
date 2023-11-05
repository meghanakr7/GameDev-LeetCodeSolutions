class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        oldColor = image[sr][sc]
        visited = set()
        def bfs(r, c, oldColor):
            # print("r and c are", r,c)
            if r < 0 or r > m-1 or c < 0 or c > n-1 or ((r, c) in visited) or image[r][c] != oldColor:
                return
            visited.add((r,c))
            if image[r][c] == oldColor:
                image[r][c] = color
            return bfs(r-1, c, oldColor) or bfs(r, c-1, oldColor) or bfs(r, c+1, oldColor) or bfs(r+1, c, oldColor)
        # visited.add((sr, sc))
        # image[sr][sc] = color
        bfs(sr,sc,oldColor)
        # print("image is ",image)
        return image
        