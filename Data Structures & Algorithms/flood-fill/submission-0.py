class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        og = image[sr][sc]
        if og == color:
            return image
        row = len(image)
        col = len(image[0])
        
        def dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= col or image[r][c] != og:
                return

            image[r][c] = color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c -1)

        dfs(sr, sc)
        return image

