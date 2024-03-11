class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        length = len(s)
        s = list(s)
        left = 0
        left_index = left
        while True:
            right = (left + k - 1) if (left + k - 1) <= (length - 1) else (length - 1)
            right_index = right
            while left_index < right_index:
                s[left_index], s[right_index] = s[right_index], s[left_index]
                left_index += 1
                right_index -= 1
            left += 2 * k
            left_index = left
            if left > length:
                return ''.join(s)
