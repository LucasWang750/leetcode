class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        length = len(s)
        s = list(s)
        left = 0
        left_index = left
        
        while True:
            right = (left + k - 1) if (left + k - 1) <= (length - 1) else (length - 1)
            right_index = right
            # print(left, right)
            while left_index < right_index:
                # temp = s[left]
                # s[left] = s[right]
                # s[right] = temp
                s[left_index], s[right_index] = s[right_index], s[left_index]
                left_index += 1
                right_index -= 1
                # print(s)
            left += 2 * k
            left_index = left
            if left > length:
                return ''.join(s)
