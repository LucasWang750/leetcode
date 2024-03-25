class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        
        def fill(image, row, col, color, old_color):
            image[row][col] = color
            if row > 0 and image[row - 1][col] == old_color:
                image[row - 1][col] = color
                fill(image, row - 1, col, color, old_color)
            if row < len(image) - 1 and image[row + 1][col] == old_color:
                image[row - 1][col] = color
                fill(image, row + 1, col, color, old_color)
            if col > 0 and image[row][col - 1] == old_color:
                image[row][col - 1] = color
                fill(image, row, col - 1, color, old_color)
            if col < len(image[row]) - 1 and image[row][col + 1] == old_color:
                image[row][col + 1] = color
                fill(image, row, col + 1, color, old_color)
            
        if image[sr][sc] == color:
            return image
        # image[sr][sc] = color 
        fill(image, sr, sc, color, image[sr][sc])
        return image