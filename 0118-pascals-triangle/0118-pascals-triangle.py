class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = []
        for i in range(1, numRows + 1):
            curr_row = [0] * i
            curr_row[0], curr_row[i-1] = 1, 1
            if i > 2:
                for j in range(1, i-1):
                    curr_row[j] = output[i-2][j-1] + output[i-2][j]
            output.append(curr_row)
        return output

        